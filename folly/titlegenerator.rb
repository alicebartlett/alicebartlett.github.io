require 'sentimental'

valid_words = {}
emojis = {}
File.open("en.txt").each do | line |
  valid_words[line.split(" ")[0]] = line.split(" ")[1]
end

File.open("emoji-sentiment.txt").each do | line |
  emojis[line.split(" ")[0]] = line.split(" ")[1]
end

Dir.foreach('../_posts') do | file |
  next if file == '.' or file == '..'
  whole_file = ""
  lowest_word = "a"
  analyzer = Sentimental.new
  File.open('../_posts/'+file).each do | line |
    whole_file += line
    line.split(" ").each do | word |
      word.gsub!(/[^A-z]/,"")
      word = word.downcase();

      if valid_words.key?(word)
        if valid_words[word].to_i < valid_words[lowest_word].to_i
          lowest_word = word
        end
      else
      #  puts "word rejected #{word}"
      end
    end
  end
  analyzer.load_defaults
  normalised_score = analyzer.score(whole_file)/35

  puts '****'
  puts file
  puts lowest_word
  puts normalised_score.round(2)
  puts emojis[normalised_score.round(2).to_s]
  puts '****'

end
