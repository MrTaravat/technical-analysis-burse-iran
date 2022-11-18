import pandas as pd
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
from datetime import datetime
from matplotlib import pyplot
from scipy.stats import linregress
global backcandles

backcandles = 20

def lastTriangle(df,start):
    candleidlist = []
    for candleid in range(start, len(df)):
        maxim = np.array([])
        minim = np.array([])
        xxmin = np.array([])
        xxmax = np.array([])
        for i in range(candleid-backcandles, candleid+1):
            if df.iloc[i].pivot == 1:
                minim = np.append(minim, df.iloc[i].Low)
                xxmin = np.append(xxmin, i) 
            if df.iloc[i].pivot == 2:
                maxim = np.append(maxim, df.iloc[i].High)
                xxmax = np.append(xxmax, i) 
        
        if (xxmax.size <3 and xxmin.size <3) or xxmax.size==0 or xxmin.size==0:
            continue

        slmin, intercmin, rmin, pmin, semin = linregress(xxmin, minim)
        slmax, intercmax, rmax, pmax, semax = linregress(xxmax, maxim)
            
    
        if abs(rmax)>=0.9 and abs(rmin)>=0.9 and slmin>=0.0001 and slmax<=-0.0001:
           candleidlist.append([[xxmin,slmin*xxmin + intercmin],[xxmax,slmax*xxmax + intercmax]])
    return candleidlist[-1]
def pivotid(df1, l, n1, n2): 
    if l-n1 < 0 or l+n2 >= len(df1):
        return 0
    
    pividlow=1
    pividhigh=1
    for i in range(l-n1, l+n2+1):
        if(df1.Low[l]>df1.Low[i]):
            pividlow=0
        if(df1.High[l]<df1.High[i]):
            pividhigh=0
    if pividlow and pividhigh:
        return 3
    elif pividlow:
        return 1
    elif pividhigh:
        return 2
    else:
        return 0
    
def pointpos(x):
    if x['pivot']==1:
        return x['Low']-1e-3
    elif x['pivot']==2:
        return x['High']+1e-3
    else:
        return np.nan


def Triangle(df):
    try:
        df=df[df['Volume']!=0]
        df.reset_index(drop=True, inplace=True)
        df['pivot'] = df.apply(lambda x: pivotid(df, x.name,3,3), axis=1)
        df['pointpos'] = df.apply(lambda row: pointpos(row), axis=1)
        pos=lastTriangle(df,0)
        return pos
    except:
        print('not find')
        return -1