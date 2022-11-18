import numpy as np 
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split



def ML_SVR(df,n):
    df=df.dropna()
    df=df[['Last']]
    forecast=int(n)
    df['Prediction']=df[['Last']].shift(-forecast)
    x= np.array(df.drop(['Prediction'],1))
    x= x[:-forecast]
    y= np.array(df['Prediction'])
    y=y[:-forecast]
    xtrain , xtest , ytrain , ytest=train_test_split(x,y,test_size=0.2)
    mysvr=SVR(C=1000,gamma='scale')
    mysvr.fit(xtrain,ytrain)
    svmconf=mysvr.score(xtest,ytest)
    x_forecast=np.array(df.drop(['Prediction'],1))[-forecast:]
    svmpred=mysvr.predict(x_forecast)
    return svmconf,svmpred.round()

def ML_LR(df,n):
    df=df.dropna()
    df=df[['Last']]
    forecast=int(n)
    df['Prediction']=df[['Last']].shift(-forecast)
    x= np.array(df.drop(['Prediction'],1))
    x= x[:-forecast]
    y= np.array(df['Prediction'])
    y=y[:-forecast]
    xtrain , xtest , ytrain , ytest=train_test_split(x,y,test_size=0.2)
    lr=LinearRegression()
    lr.fit(xtrain,ytrain)
    lrconf=lr.score(xtest,ytest)
    x_forecast=np.array(df.drop(['Prediction'],1))[-forecast:]
    lrpred=lr.predict(x_forecast)
    return lrconf,lrpred.round()