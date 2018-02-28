# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:54 2018
Last modified : Tue Feb 27 17:06 2018
@author: Christophe HARDY
"""
import json
import argparse
import re

#Paser for input arguments
parser = argparse.ArgumentParser()
parser.add_argument("-fTR", "--fileToRead", dest="fileToRead", help ="The file who contain your text")
parser.add_argument("-rF", "--resultFile", dest="resultFile", help ="The file who will contain the word distribution") 
parser.add_argument(dest="inputDir")
parser.add_argument(dest="outputDir")
args = parser.parse_args()

#Openning of files
fileR = open(args.inputDir + "/" + args.fileToRead,"r")
fileJSON = open(args.outputDir + "/" + args.resultFile,"w")

#Variables definition
nbword = 0
sumtest = 0
word_dict = dict()

#We go through our text and add each word in a dictionnary 
#with the number of apperence of the word in the text
for line in fileR:
        for word in line.split():
            nbword += 1 
            word = word.lower()
            word = re.sub(r'[^a-z]','',word)
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

#For each word we define the %age of the word apperence   
#for key in word_dict:
#    word_dict[key] = round(float(word_dict[key])/nbword,10) #depeding of what you want the round can be modified

#test to see we are doing the right thing
#for key in word_dict:
#    sumtest += word_dict[key]

    
#Writting the result in a jsonfile
fileJSON.write(json.dumps(word_dict))
    
#End access to file  
fileR.close()
fileJSON.close()
