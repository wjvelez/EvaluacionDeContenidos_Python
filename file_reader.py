import re
import os
import nltk
from nltk.corpus import stopwords

class FileReader:
    def __init__(self, directory):
        "docstring"
        self.directory = directory #loading files directory.
        self.words = []
        self.matriz={}
    def loadwords(self):
        for textfile in os.listdir(self.directory): #iterate each file in the specified dir
            self.matriz[textfile] = []
            self.iterateFile(textfile)
           
    def iterateFile(self,textfile):
        f = open(self.directory+'/'+textfile, 'r')
        for line in f:
           self.words.extend([token for token in nltk.word_tokenize(line) if token.lower() not in stopwords.words('spanish') and len([letter for letter in token.lower() if letter.isdigit()])==0 ])
           self.matriz[textfile].extend([token for token in nltk.word_tokenize(line) if token.lower() not in stopwords.words('spanish') and len([letter for letter in token.lower() if letter.isdigit()])==0 ])

    def printwords(self):
        print(self.matriz)
        
    def deletewords(self,words):
        for word in self.words:
            if word in words:
                self.removeall_replace(word)

    def removeall_replace(self,word):
        t = [y for y in self.words if y != word]
        del self.words[:]
        self.words.extend(t)
