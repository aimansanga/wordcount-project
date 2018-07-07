from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def count(request):
    #Extract the incoming text from the request
    text = request.GET['wordstobecounted']

    #Split that text into a list of indipendent words
    wordlist = text.split()

    #Use those words as keys in a dictionary and assign them a number value that reflects their frequencies
    #First create an empty dictionary
    worddictionary = {}

    #Use the for loop to loop through "wordlist" list
    for word in wordlist:
        #If the word is in the dictionary as a key,
        if word in worddictionary:
            #Increament its value (frequency) by one.
            worddictionary[word] += 1
        #Else if there is no key in the dictionary matching this word,
        else:
            #Create it (the key) and assign it a value of 1,
            worddictionary[word] = 1

    #Now turn this dictionary into a list
    worddictionarylist = worddictionary.items()

    #Now sort the worddictionarylist in a descending order of the values
    sortedworddictionarylist = sorted(worddictionarylist, key=operator.itemgetter(1), reverse=True)

    context = {'text': text, 'numberofwords':len(wordlist), 'sortedworddictionarylist': sortedworddictionarylist}

    return render(request, 'count.html', context)
