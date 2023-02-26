#!/usr/bin/env python
# coding: utf-8

# In[29]:


pip install SpeechRecognition pyphen


# In[30]:


import speech_recognition as sr
import nltk
import pyphen
nltk.download('punkt')
# Load the audio file
audio_file = sr.AudioFile('ptk_2.wav')


# In[31]:


# Convert the audio file into text
recognizer = sr.Recognizer()
with audio_file as source:
    audio = recognizer.record(source)
text = recognizer.recognize_google(audio)


# In[32]:


# Count the number of syllables in each word
dic = pyphen.Pyphen(lang='en_GB')
syllables = [len(dic.inserted(text)) for word in words]

# Count the total number of syllables
total_syllables = sum(syllables)
print('There are', total_syllables, 'syllables.')

