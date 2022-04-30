from cProfile import label
import joblib
import pandas as pd
import numpy as np
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
from joblib import Memory

df=pd.read_csv("./news.csv")
labels=df.label
x_train,x_test,y_train,y_test=train_test_split(df["text"],labels,test_size=0.2,random_state=20)

vector = TfidfVectorizer(stop_words="english",max_df=0.7)
tf_train=vector.fit_transform(x_train)
tf_test=vector.transform(x_test)
pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tf_train,y_train)
y_pred=pac.predict(tf_test)
score=accuracy_score(y_test,y_pred)
print(f"Accuracy: {round(score*100,2)}%")
print(x_test)
accuracyOfModel=round(score*100,2)
print(accuracyOfModel)
confusion_matrix(y_test,y_pred,labels=['FAKE','REAL'])
filename="final_model.pkl"
pickle.dump(pac,open(filename,"wb"))

filename1='vectorizer.pkl'
pickle.dump(vector,open(filename1,"wb"))
# pipe = joblib.load('final_model.pkl')
# pred=pipe.predict([["Hello"]])
# print(pred)
# pred=pipe.predict()