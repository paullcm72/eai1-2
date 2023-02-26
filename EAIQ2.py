#!/usr/bin/env python
# coding: utf-8

pip install SpeechRecognition pyphen

import speech_recognition as sr
import nltk
import pyphen
nltk.download('punkt')
# Load the audio file
audio_file = sr.AudioFile('ptk_2.wav')

# Convert the audio file into text
recognizer = sr.Recognizer()
with audio_file as source:
    audio = recognizer.record(source)
text = recognizer.recognize_google(audio)


# Count the number of syllables in each word
dic = pyphen.Pyphen(lang='en_GB')
syllables = [len(dic.inserted(text)) for word in words]

# Count the total number of syllables
total_syllables = sum(syllables)
print('There are', total_syllables, 'syllables.')

