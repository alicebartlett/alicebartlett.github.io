#!/usr/bin/env python3
"""
Normalize weaknotes titles to format: "Week N: First word capitalized, rest lowercase"
except for proper nouns and special cases.
"""

import re
import os
from pathlib import Path

def normalize_title_subtitle(subtitle):
    """
    Normalize subtitle: capitalize first letter, lowercase the rest
    except for known proper nouns and special words.
    """
    # List of words that should stay capitalized (proper nouns, acronyms, etc.)
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
        'Latin', 'English', 'French', 'Spanish', 'German', 'Danish'
    }
    
    # Special cases that should stay as-is
    if subtitle in ['t(\'_\'t)', '¯\\_(ツ)_/¯', '- nice', '🐦']:
        return subtitle
        
    # If it starts with emoji or special char, keep as-is
    if subtitle and not subtitle[0].isalpha():
        return subtitle
    
    # Capitalize first letter
    if not subtitle:
        return subtitle
        
    words = subtitle.split()
    if not words:
        return subtitle
    
    # First word always gets capital
    result = [words[0].capitalize()]
    
    # Rest of words: lowercase unless in keep_caps
    for word in words[1:]:
        # Check if word (without punctuation) is in keep_caps
        clean_word = word.strip('.,!?;:\'"')
        if clean_word in keep_caps:
            result.append(word)
        else:
            result.append(word.lower())
    
    return ' '.join(result)

def process_file(filepath):
    """Process a single markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match: title: "Week N: subtitle"
    pattern = r'^title: "Week (\d+): (.+)"$'
    
    lines = content.split('\n')
    modified = False
    
    for i, line in enumerate(lines):
        match = re.match(pattern, line)
        if match:
            week_num = match.group(1)
            subtitle = match.group(2)
            normalized = normalize_title_subtitle(subtitle)
            
            if subtitle != normalized:
                new_line = f'title: "Week {week_num}: {normalized}"'
                lines[i] = new_line
                modified = True
                print(f"  {filepath.name}")
                print(f"    OLD: Week {week_num}: {subtitle}")
                print(f"    NEW: Week {week_num}: {normalized}")
    
    if modified:
        new_content = '\n'.join(lines)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    return modified

def main():
    weaknotes_dir = Path('_posts/weaknotes')
    
    if not weaknotes_dir.exists():
        print(f"Error: {weaknotes_dir} not found")
        return
    
    files_changed = 0
    total_files = 0
    
    # Process all markdown files
    for md_file in sorted(weaknotes_dir.rglob('*.md')):
        total_files += 1
        if process_file(md_file):
            files_changed += 1
    
    print(f"\nProcessed {total_files} files, modified {files_changed} files")

if __name__ == '__main__':
    main()
