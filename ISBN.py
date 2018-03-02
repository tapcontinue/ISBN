#!/usr/bin/python

#inport the library(s)
import isbn_hyphenate
import pyperclip

isbns = pyperclip.paste()
mylist = isbns.split(' ')

mylist[0].split(' ')
mylist[1].split(' ')
mylist[2].split(' ')

print "All ISBNs are now in your clipboard. The code below is simply for your review" + "\n"

print "<p class=\"isbn\">Print ISBN: " + isbn_hyphenate.hyphenate(mylist[0]) +"</p>"
print "<p class=\"isbn\">ePub ISBN: " + isbn_hyphenate.hyphenate(mylist[1]) +"</p>"
print "<p class=\"isbn\">Kindle ISBN: " + isbn_hyphenate.hyphenate(mylist[2]) +"</p>"


pyperclip.copy("<p class=\"isbn\">Print ISBN: " + isbn_hyphenate.hyphenate(mylist[0]) +"</p>" + "\n" + "<p class=\"isbn\">ePub ISBN: " + isbn_hyphenate.hyphenate(mylist[1]) +"</p>" + "\n" + "<p class=\"isbn\">Kindle ISBN: " + isbn_hyphenate.hyphenate(mylist[2]) +"</p>")
