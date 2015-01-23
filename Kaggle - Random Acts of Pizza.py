#******************************************************
# Author: Bill Zichos
#******************************************************
print('Author: Bill Zichos')


#******************************************************
# Objective: Determine whether or not a person's request
#    for a free pizza will be fullfilled.  This will be
#    expressed as a 0 or 1 in the submission file.
#******************************************************
print("Objective: Determine whether or not a person's request for a free pizza" +
      "will be fullfilled.  This will be expressed as a 0 or 1 in the submission file.")


#******************************************************
# Module import
#******************************************************
import json
import nltk
import re


#******************************************************
# Functions
#******************************************************
def bzSentenceCount(text):
        return len(nltk.sent_tokenize(text))

def bzWordCount(text):
        return len(nltk.word_tokenize(text))

def bzLexicalDiversity(text):
        return len(set([words.lower() for words in nltk.word_tokenize(text)])) / len(nltk.word_tokenize(text))


#******************************************************
# Read in the datasets and add features
#******************************************************
trainfilepath = 'C:\\Users\\Bill\\Documents\\GitHub\\Project-Files\\Kaggle - Random Acts of Pizza Train.json'
testfilepath = 'C:\\Users\\Bill\\Documents\\GitHub\\Project-Files\\Kaggle - Random Acts of Pizza Test.json'

#filepaths = [trainfilepath, testfilepath]
filepaths = [trainfilepath]

for file in filepaths:
        print('Loading file ' + file)
        json_data = open(file)
        data = json.load(json_data)
        #******************************************************
        # Add features to the datasets
        # 1. Sentence Count
        # 2. Word Count
        # 3. Lexical Diversity
        # 4. Request Text Flag
        # 5. Picture Flag
        # 6. Curse Word Flag
        #******************************************************
        for item in data:
                if len(item['request_text'])>0:
                        item['SentCount']=bzSentenceCount(item['request_text'])
                        item['WordCount']=bzWordCount(item['request_text'])
                        item['LexicalDiversity']=bzLexicalDiversity(item['request_text'])
                        item['RequestTextFlag']=1
                else:
                        item['RequestTextFlag']=0
        picList = [item['request_id'] for item in data if re.search('.jpg|.png', item['request_text'])]
        for item in data:
                if item['request_id'] in picList:
                        item['Picture']=1
                else:
                        item['Picture']=0
        # replace with the badWords I accumulated in a private file.
        badWords = ['crap', 'poop']
        for item in data:
                item['CurseWordFlag']=0
        for item in data:
                for word in nltk.word_tokenize(item['request_text']):
                        if word in badWords:
                                item['CurseWordFlag']=1
        #******************************************************
        # Machine Learning - Generate Algortithm
        #******************************************************




        #******************************************************
        # Machine Learning - Apply Algorithm to Test Set
        #******************************************************



        #******************************************************
        # Create file for Submission
        #******************************************************
        # request_id
        # requester_received_pizza

        submission = [(item['request_id'], item['requester_received_pizza2']) for item in data]

# Output a submission file
##with open("C:\\test.csv", "w", newline="") as output:
##	writer = csv.writer(output, delimiter = ',')
##	writer.writerows(table)
