require 'yaml'

def load_library(file_path)
  # code goes here
    library = {'get_meaning' => {}, 'get_emoticon' => {}}
    YAML.load_file(file_path).each do |meaning, array|
        english, japanese = array
        library['get_meaning'][japanese] = meaning
        library['get_emoticon'][english] = japanese
    end
    library
end

def get_japanese_emoticon(file_path, emoji)
    library = load_library(file_path)
    result = library['get_emoticon'][emoji]
    if result
        result
    else
        "Sorry, that emoticon was not found"
    end
end

def get_english_meaning(file_path, emoji)
    library = load_library(file_path)
    result = library['get_meaning'][emoji]
    if result
        result
    else
        "Sorry, that emoticon was not found"
    end
end


 