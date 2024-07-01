
# import tkinter module
import tkinter
from tkinter import *
from tkinter import font 
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import matplotlib.pyplot as plt
import sys,tweepy,csv,re
from typing import Counter
from textblob import TextBlob
from googletrans import Translator
import warnings
from tensorflow.keras.models import load_model
from PIL import ImageTk, Image
warnings.filterwarnings("ignore")
# creating main tkinter window/toplevel
master = Tk()
# master.state("zoomed")
img = ImageTk.PhotoImage(Image.open("1.jpg"))
l = Label( image = img)
master.title("Personalized Federated Learning for Intelligent IoT Applications: A Cloud-Edge Based Framework")
text = tkinter.Label( text="Personalized Federated Learning for Intelligent IoT Applications: A Cloud-Edge Based Framework", font=("Helvetica", 12), height=2, anchor='n', fg='#f00')
def askopenfile():
    global filename
    global df
    global name
    filename=askopenfilename( filetypes =(("CSV Files","*.csv"),))
    df=pd.read_csv(filename)
    name=textExample.get("1.0","end")
    arr=np.array([name,df])
    result['text']="File uploaded"
b=Button(text="Upload dataset", command=askopenfile)
result = tkinter.Label(text="you will see result here!",font=('Courier', 12), height=40, anchor='nw')
textExample=tkinter.Text(master, height=1,)
text.grid(row=0, columnspan=4)

def Close():
    master.destroy()
def predict():
    labels=["WALKING", "WALKING_UPSTAIRS", "WALKING_DOWNSTAIRS", "SITTING", "STANDING","LYING"]
    y_test = df['activity']
    X_test = df.drop(['activity','activity_name','subject_id'],axis=1)
    model = load_model('model.h5')
    ypred=model.predict(X_test)
    pred= np.argmax(ypred,axis=1)
    results=''
    for i in pred:
        results=results+'\n'+labels[i]
    result['text']=results
b1=Button(text="predict", command=predict)
b2=Button(text="Close application", command=Close)
l.grid(row=1, column=0)
textExample.grid(row=2, column=0)
b.grid(row=3,column=0)
b1.grid(row=4,column=0)
b2.grid(row=5, column=0)
result.grid(rowspan=6,columnspan=4)

# infinite loop which can be terminated 
# by keyboard or mouse interrupt
mainloop()