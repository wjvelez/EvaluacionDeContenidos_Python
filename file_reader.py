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
        for key in self.matriz:
            temp = [y for y in self.words if y != word]
            del self.matriz[key][:]
            self.matriz[key].extend(temp)
        t = [y for y in self.words if y != word]
        del self.words[:]
        self.words.extend(t)

    def get_unrepeatedWords(self):
        '''se tiene una lista sin elementos repetidos '''
        return list(set(self.words))

    
    def countWordsInFile(self,key,word):
        '''key = filename '''
        return self.matriz[key].count(word)
        
    def printStadistics(self):
        for key in self.matriz:
            print("Nombre de Documento %s",(key))
            for word in self.matriz[key]:
                print("Palabra: %s  Conteo %d",(word,self.countWordsInFile(key,word)))
