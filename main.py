import requests
import numpy as np
import matplotlib.pyplot as plt
import string
import operator
macbeth = requests.get('http://www.gutenberg.org/cache/epub/2264/pg2264.txt').text

# print(type(macbeth))
# print(len(macbeth))
# print(macbeth[10000:])
# Split the transcript into words
# Create a dictionary
# Iterate through the text of Macbeth
# Update word counts
# Sort words by counts in descending order
# Create Bar Graph
# Include descriptive titles and labels
mac_dict={}
macbeth=macbeth.partition('David Reed')[2]  #found where the play starts
# for char in '-.,\n?':
#     macbethh=macbeth.replace(char,' ')
macbeth=macbeth.lower()
macbeth.translate(str.maketrans('', '', string.punctuation)) #removes punctuations using string library
macbeth_list=macbeth.split() #makes it into a list
# macbeth=macbeth.split(" ")
for words in macbeth_list:             #removes numbers
    if words[0].isalpha()==False:
        macbeth_list.remove(words)
for words in macbeth_list:           #creates dictionary
    mac_dict[words] =mac_dict.get(words,0)+1
sorted_d = sorted(mac_dict.items(), key=operator.itemgetter(1),reverse=True) #sorts them in descending order
x=[]
y=[]
for sort in sorted_d:
    x.append(sort[0])
    y.append(sort[1])
plt.bar(x,y)
plt.title('Words in Macbeth')
plt.xlabel('Words')
plt.ylabel('Word Count')
plt.show()
