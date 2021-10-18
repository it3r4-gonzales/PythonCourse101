import sys
from urllib.request import urlopen

def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    """Fetch a list of word from a URL

    Args:
        url: The URL of UTF-8 text document
    
    """
    #to docstring type in cli help(fetch_words)
    #story = urlopen('http://sixty-north.com/c/t.txt')
  


# def print_words(story_words):
#     for word in story_words:
#         print(word)

def print_items(items): 
    for item in items:
        print(item)

def main():
    url = sys.argv[1]
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main()

#if code is run as module it prints the name of the module by using the dunder name/ __name__
#if code is run as script it prints dunder main/__main__
#python module with api
#python scripts execution from command line
#python program composed of many modules