from urllib.request import urlopen

def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()

    for word in story_words:
        print(word)

#if code is run as module it prints the name of the module by using the dunder name/ __name__
print(__name__)



#if code is run as script it prints dunder main/__main__
if __name__ == '__main__':
    fetch_words()

#python module with api
#python scripts execution from command line
#python program composed of many modules