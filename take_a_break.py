import time
import webbrowser

total_number_of_breaks = 3
number_of_breaks = 0

print ("The program started at "+time.ctime())
while number_of_breaks < total_number_of_breaks:
    time.sleep(1*60*60)
    print ("Break started at "+time.ctime())
    webbrowser.open("https://www.youtube.com/watch?v=JhrrD9XLZQ8")
    number_of_breaks = number_of_breaks +1
