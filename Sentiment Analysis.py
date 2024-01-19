#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import os
#import string
import glob
import itertools
import re
from nltk.tokenize import RegexpTokenizer,word_tokenize,sent_tokenize


# # Importing Web Text

# In[28]:


filename = "Filelocation\filename.txt"
file = open(filename, 'rt')
text = file.read()
file.close()
tokenized_text=word_tokenize(text)


# # Importing Stop Words and Filtering

# In[29]:


file_list = glob.glob(os.path.join(os.getcwd(), "Importing F", "*.txt"))

stopwords = []
for file_path in file_list:
    with open(file_path, 'r') as f:
        stopwords.extend(f.read().lower().splitlines())


# In[30]:


filtered_sent=[]
for w in tokenized_text:
    if w not in stopwords:
        filtered_sent.append(w)
total_after_cleaning =len(filtered_sent)


# # Creating Positive and Negative Dictionaries

# In[31]:


full_vocab = dict()
i = 0
for word in filtered_sent:
    full_vocab[word] = i


# In[32]:


positiveWordsFile = 'File location.txt'
negativeWordsFile = 'File location.txt'


# In[33]:


with open(positiveWordsFile,'r') as posfile:
    positivewords=posfile.read().lower()
positiveWordList=positivewords.split()

with open(negativeWordsFile ,'r') as negfile:
    negativeword=negfile.read().lower()
negativeWordList=negativeword.split()


# In[34]:


pos_dic = list(itertools.filterfalse(lambda x:x not in positiveWordList,full_vocab))
neg_dic = list(itertools.filterfalse(lambda x:x not in negativeWordList,full_vocab))


# # Calculating Derived variables

# In[35]:


psd = dict()
i = 0

for word in pos_dic:
    psd[word] = i
    i = i+1
values = psd.values()
positve_score = sum(values)


# In[36]:


nsd = dict()
i = 0

for word in neg_dic:
    nsd[word] = i
    i = i-1*-1
values = nsd.values()
negative_score = sum(values)


# # Polarity Score

# In[37]:


pol_score = (positve_score - negative_score) / ((positve_score + negative_score) + 0.000001)


# # Subjectivity Score

# In[38]:


sub_score = (positve_score + negative_score)/ ((total_after_cleaning) + 0.000001)


# # Analysis of Readbility

# In[39]:


totalWordCount = len(tokenized_text)
sentence_list = sent_tokenize(text)
totalSenCount = len(sentence_list)


# In[40]:


Average_Sentence_Length = totalWordCount / totalSenCount


# In[41]:


complexWord = 0
complex_word_percentage = 0
for word in tokenized_text:
        vowels=0
        if word.endswith(('es','ed')):
            pass
        else:
            for w in word:
                if(w=='a' or w=='e' or w=='i' or w=='o' or w=='u'):
                    vowels += 1
            if(vowels > 2):
                complexWord += 1
            if len(tokenized_text) != 0:
                complex_word_percentage = complexWord/len(tokenized_text)


# In[42]:


Fog_Index = 0.4 * (Average_Sentence_Length + complex_word_percentage)


# # Average Number of Words Per Sentence

# In[43]:


Avg_No_of_Words_Per_Sentence = totalWordCount / totalSenCount


# # Personal Pronouns

# In[44]:


pronounRegex = re.compile(r'I|we|my|ours|us',re.I)
pronouns = pronounRegex.findall(text)
personal_pronouns=len(pronouns)


# In[45]:


print("Positive Score",positve_score)
print("Negative Score",negative_score)
print("Polarity Score",pol_score)
print("Subjectivity Score",sub_score)
print("Average Sentence Length",Average_Sentence_Length)
print("Percentage Of Complexe Words",complex_word_percentage)
print("Analysis of Readability",round(Fog_Index))
print("Average Number of Words Per Sentence",round(Avg_No_of_Words_Per_Sentence))
print("Complex Word Count",complexWord)
print("Personal Pronouns",personal_pronouns)


# In[ ]:




