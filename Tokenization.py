# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 16:26:27 2020

@author: Neha
"""
import nltk
#nltk.download()
paragraph="""Dr Avul Pakir Jainulabdeen
 Abdul Kalam was born on 15 October 1931, at 
 Rameswaram in Tamil Nadu, India. He specialized in 
 Aeronautical Engineering from Madras Institute of 
 Technology and became an eminent scientist.
 Dr Kalam was awarded the Padma Bhushan (1981), 
 the Padma Vibhushan (1990), and India’s highest
 civilian award- the Bharat Ratna in 1997. In 2002, Dr
 Kalam became the 11th President of India. He was fondly
 called the people's President for being the first 
 President in the country to connect with the youth 
 via the internet."""
# sentences from the paragraph
sentences=nltk.sent_tokenize(paragraph)
# words from sentences
words=nltk.word_tokenize(paragraph)