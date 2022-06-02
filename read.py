
import string

def read_file_content(filename):
    open_file = open("./story.txt", "r")
        read_file = open_file.read()
    return read_file

def count_words():
    text = read_file_content("./story.txt")
    text = text.translate(str.maketrans("", "", string punctuation))
    words = text.split()
    count = {}
    for word in words:
        count[word] = words.count(word)
    return count

print(count_words())
