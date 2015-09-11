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

##	1. Unique words
##		a. Training file only
##		b. Come up with a complete list of words used across all requests.
##		c. Sort them alphabetically
##		d. Optional (this can have a big impact on model accuracy):
##			i. Spell check (easier said than done).
##			ii. Convert "loooooove"
##			iii. Convert conjugations (i.e. can't to cannot)
##			iv. Case handling
##	2. Create factors
##		a. Include unique identifier - request_id.
##		b. Create a factor (column) for each word from step 1.
##		c. Set the values of the new factors to zero (default).
##		d. Training and Test file.
##		e. Identify and include the target attribute - requester_received_pizza.  This will be blank on the test file.
##	3. Populate factors
##		a. Do so for each request.
##		b. Count how many times each word was used in the text.
##		c. Add the count to the associated factor.
##	4. Export as csv file
##		a. Request ID
##		b. Requester Received Pizza Flag
##		c. A field for each word in the training file.
##	5. Upload into Amazon Machine Learning.  Follow their process to generate a model and then use the model to generate results for the test file.

#******************************************************
# Module import & general variables
#******************************************************
import json
import nltk
import re
trainfilepath = 'C:\\Users\\Bill\\Documents\\GitHub\\Project-Files\\Kaggle - Random Acts of Pizza Train.json'
testfilepath = 'C:\\Users\\Bill\\Documents\\GitHub\\Project-Files\\Kaggle - Random Acts of Pizza Test.json'

#******************************************************
# Unique words
#   a. Training file only
#   b. Come up with a complete list of words used across all requests.
#   c. Sort them alphabetically
#   d. Optional (this can have a big impact on model accuracy):
#      i. Spell check (easier said than done).
#      ii. Convert "loooooove"
#      iii. Convert conjugations (i.e. can't to cannot)
#      iv. Case handling
#******************************************************

print('Loading file ' + trainfilepath)
json_data = open(trainfilepath)
data = json.load(json_data)

text = ' '.join([item['request_text'] for item in data if len(item['request_text'])> 0])

bagOfWords = [word.lower() for word in nltk.word_tokenize(text) if word.isalpha()]

bagOfWords = sorted(set(bagOfWords))

#******************************************************
## Create factors
##   a. Create a factor (column) for each word from step 1.
##   b. Training and Test file.
## Populate factors
##   a. Do so for each request.
##   b. Count how many times each word was used in the text.
##   c. Add the count to the associated factor.
#******************************************************

for item in data:
        for word in bagOfWords:
                item[word]=item['request_text'].count(word)

# Output a submission file
##with open("C:\\test.csv", "w", newline="") as output:
##	writer = csv.writer(output, delimiter = ',')
##	writer.writerows(table)

##writer = csv.writer(open('dict.csv', 'wb'))
##for item in data:
##        for key, value in item.items():
##                writer.writerow([key, value])


##class csv.DictWriter(csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)
##
##    Create an object which operates like a regular writer but maps dictionaries onto output rows. The fieldnames parameter is a sequence of keys that identify the order in which values in the dictionary passed to the writerow() method are written to the csvfile. The optional restval parameter specifies the value to be written if the dictionary is missing a key in fieldnames. If the dictionary passed to the writerow() method contains a key not found in fieldnames, the optional extrasaction parameter indicates what action to take. If it is set to 'raise' a ValueError is raised. If it is set to 'ignore', extra values in the dictionary are ignored. Any other optional or keyword arguments are passed to the underlying writer instance.
##
##    Note that unlike the DictReader class, the fieldnames parameter of the DictWriter is not optional. Since Python’s dict objects are not ordered, there is not enough information available to deduce the order in which the row should be written to the csvfile.
##
##    A short usage example:
##
##    import csv
##
##    with open('names.csv', 'w') as csvfile:
##        fieldnames = ['first_name', 'last_name']
##        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
##
##        writer.writeheader()
##        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
##        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
##        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
##
                
                
fieldnames = ['request_id', 'requester_received_pizza'] + bagOfWords
