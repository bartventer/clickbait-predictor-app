# IMPORTING LIBRARIES AND PACKAGES
import numpy as np 
import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
import string as s
import re
import os
import joblib

nltk.data.path.append("./machineLearning/nltk_data")

class ClickBaitModel:
    def __init__(self, text):
        
        '''
        Argument required is a JSON object as retrieved from the POST request
        JSON object = {"title":"string"}
        '''
        
        self.text = text["title"]
        
        
    def tokenization(self):
        lst=self.text.split()
        return lst
    
    
    def lowercasing(self,arg):
        new_lst=[]
        for i in arg:
            i=i.lower()
            new_lst.append(i)
        return new_lst

    
    def remove_stopwords(self, arg):
        stop=stopwords.words('english')
        new_lst=[]
        for i in arg:
            if i not in stop:
                new_lst.append(i)
        return new_lst

    
    def remove_punctuations(self, arg):
        new_lst=[]
        for i in arg:
            for j in s.punctuation:
                i=i.replace(j,'')
            new_lst.append(i)
        return new_lst

    
    def remove_numbers(self, arg):
        nodig_lst=[]
        new_lst=[]
        for i in arg:
            for j in s.digits:    
                i=i.replace(j,'')
            nodig_lst.append(i)
        for i in nodig_lst:
            if i!='':
                new_lst.append(i)
        return new_lst
    
    
    def remove_spaces(self, arg):
        new_lst=[]
        for i in arg:
            i=i.strip()
            new_lst.append(i)
        return new_lst


    
    def lemmatzation(self, arg):
        lemmatizer=nltk.stem.WordNetLemmatizer()
        new_lst=[]
        for i in arg:
            i=lemmatizer.lemmatize(i)
            new_lst.append(i)
        return new_lst
    
    
    def preprocess(self):
        temp = self.tokenization()
        temp = self.lowercasing(temp)
        temp = self.remove_stopwords(temp)
        temp = self.remove_punctuations(temp)
        temp = self.remove_numbers(temp)
        temp = self.remove_spaces(temp) 
        lemmatizer=WordNetLemmatizer()
        temp = self.lemmatzation(temp)
        temp = ''.join(i+' ' for i in temp)
        return temp  
    
    
    def predict(self,scaler,model):
        '''
        Arguments required are the scaler and model objects.
        This function will preprocess the JSON object, and return a prediction as a string.
        '''
        temp = self.preprocess()
        temp = scaler.transform([temp])
        temp_arr=temp.toarray()
        pred=model.predict(temp_arr)[0]
        return "Clickbait!" if pred == 1 else "Not Clickbait!"