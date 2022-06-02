

def read_file_content(filename):
    with open(filename) as file:
        file_content = file.read()
    return file_content

def count_words():
    text = read_file_content("./story.txt")
    text = text.translate(str.maketrans("", "", string punctuation))
    words = text.split()
    count = {}
    for word in words:
        if word in count
            count[word] += 1
        else:
            count[word] = 1
    return count

print(count_words())
