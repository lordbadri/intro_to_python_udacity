import urllib

def read_text():
    quotes = open(r"D:\google_drive\Online courses\udacity\intro to python\profanity_editor\movie_quotes.txt")
    contents = quotes.read()
    #print contents
    quotes.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()

    if "true" in output:
        print("Profanity alert")
    elif "false" in output:
        print("No profanity in the document")
    else:
        print("couldn't read document")
read_text()    
