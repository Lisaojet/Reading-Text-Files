

def read_file_content(filename):
    open_file = open("./story.txt", "r")
    read_file = open_file.read()
    print(read_file)
read_file_content("story.txt")



def count_words():
    text = read_file_content("./story.txt")
    words = text.split("")
    count = {}
    for word in text:
        if word in text:
            count[word] += 1
        else:
            count[word] = 1
    return count
print(count_words)