#!/usr/bin/env python3
"""
Interactive title normalization - asks for confirmation before each change.
"""

import re
import os
from pathlib import Path
import sys

# File to store exemptions
EXEMPTIONS_FILE = '.title-exemptions.txt'

def load_exemptions():
    """Load list of titles to exempt from normalization."""
    if not os.path.exists(EXEMPTIONS_FILE):
        return set()
    with open(EXEMPTIONS_FILE, 'r', encoding='utf-8') as f:
        return set(line.strip() for line in f if line.strip() and not line.startswith('#'))

def save_exemption(week_num, subtitle):
    """Save a title to the exemptions list."""
    entry = f"Week {week_num}: {subtitle}"
    with open(EXEMPTIONS_FILE, 'a', encoding='utf-8') as f:
        f.write(entry + '\n')
    print(f"  Added to exemptions: {entry}")

def normalize_title_subtitle(subtitle):
    """
    Normalize subtitle: capitalize first letter, lowercase the rest
    except for known proper nouns and special words.
    """
    # List of words that should stay capitalized
    keep_caps = {
        'I', 'BBC', 'FT', 'COVID', 'DIY', 'NHS', 'UK', 'US', 'AI', 'HTML', 
        'CSS', 'JavaScript', 'Python', 'BERG', 'USA', 'EU', 'UN', 'LRUG',
        'Brighton', 'London', 'Yorkshire', 'Scotland', 'Wales', 'England',
        'Alice', 'Lachie', 'Edith', 'Christmas', 'Easter', 'Sunday', 'Monday',
        'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December',
        'Netflix', 'Google', 'Amazon', 'Boris', 'Johnson', 'COVID-19',
        'Monty', 'Don', 'Bisto', 'Simpsons', 'Flanders', 'Ned',
        'Latin', 'English', 'French', 'Spanish', 'German', 'Danish',
        'StaffPlus', 'Lenin'
    }
    
    # Special cases that should stay as-is
    if subtitle in ['t(\'_\'t)', '¯\\_(ツ)_/¯', '- nice', '🐦']:
        return subtitle
        
    # If it starts with emoji or special char, keep as-is
    if subtitle and not subtitle[0].isalpha():
        return subtitle
    
    if not subtitle:
        return subtitle
        
    words = subtitle.split()
    if not words:
        return subtitle
    
    # First word always gets capital
    result = [words[0].capitalize()]
    
    # Rest of words: lowercase unless in keep_caps
    for word in words[1:]:
        clean_word = word.strip('.,!?;:\'"')
        if clean_word in keep_caps:
            result.append(word)
        else:
            result.append(word.lower())
    
    return ' '.join(result)

def ask_user(week_num, current, proposed, filepath):
    """Ask user whether to apply the change."""
    print(f"\n{'='*70}")
    print(f"File: {filepath.name}")
    print(f"Week {week_num}")
    print(f"  Current:  {current}")
    print(f"  Proposed: {proposed}")
    print(f"{'='*70}")
    
    while True:
        response = input("Apply change? [y/n/q to quit]: ").lower().strip()
        if response in ['y', 'yes']:
            return 'apply'
        elif response in ['n', 'no']:
            return 'skip'
        elif response in ['q', 'quit']:
            return 'quit'
        else:
            print("Please enter y, n, or q")

def process_files_interactive():
    """Process all files interactively."""
    weaknotes_dir = Path('_posts/weaknotes')
    
    if not weaknotes_dir.exists():
        print(f"Error: {weaknotes_dir} not found")
        return
    
    exemptions = load_exemptions()
    pattern = r'^title: "Week (\d+): (.+)"$'
    
    files_to_process = []
    
    # First pass: find all files that need changes
    for md_file in sorted(weaknotes_dir.rglob('*.md')):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        for i, line in enumerate(lines):
            match = re.match(pattern, line)
            if match:
                week_num = match.group(1)
                subtitle = match.group(2)
                
                # Skip if in exemptions
                exemption_key = f"Week {week_num}: {subtitle}"
                if exemption_key in exemptions:
                    continue
                
                normalized = normalize_title_subtitle(subtitle)
                
                if subtitle != normalized:
                    files_to_process.append({
                        'file': md_file,
                        'line_num': i,
                        'week_num': week_num,
                        'current': subtitle,
                        'proposed': normalized,
                        'lines': lines
                    })
                break
    
    if not files_to_process:
        print("No titles need normalization!")
        return
    
    print(f"\nFound {len(files_to_process)} titles that might need normalization\n")
    
    applied = 0
    skipped = 0
    
    for item in files_to_process:
        response = ask_user(item['week_num'], item['current'], item['proposed'], item['file'])
        
        if response == 'quit':
            print(f"\nStopped. Applied {applied} changes, skipped {skipped}")
            break
        elif response == 'apply':
            # Apply the change
            new_line = f'title: "Week {item["week_num"]}: {item["proposed"]}"'
            item['lines'][item['line_num']] = new_line
            
            with open(item['file'], 'w', encoding='utf-8') as f:
                f.write('\n'.join(item['lines']))
            
            print(f"  ✓ Applied")
            applied += 1
        else:  # skip
            # Add to exemptions
            save_exemption(item['week_num'], item['current'])
            skipped += 1
    
    print(f"\n{'='*70}")
    print(f"Summary: Applied {applied} changes, skipped {skipped}")
    if skipped > 0:
        print(f"Exemptions saved to: {EXEMPTIONS_FILE}")

if __name__ == '__main__':
    process_files_interactive()
