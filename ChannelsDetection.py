import pandas as pd
import plotly.graph_objects as go
import numpy as np
from matplotlib import pyplot
def find(df,last):
    pos=[]
    backcandles= 40 # 6*8
    brange = 10 # backcandles//4 #should be less than backcandles
    wind = 6

    candleid = len(df)-last

    optbackcandles= backcandles
    sldiff = 10000

    for r1 in range(backcandles-brange, backcandles+brange):
        maxim = np.array([])
        minim = np.array([])
        xxmin = np.array([])
        xxmax = np.array([])
        for i in range(candleid-r1, candleid+1, wind):
            minim = np.append(minim, df.Low.iloc[i:i+wind].min())
            xxmin = np.append(xxmin, df.Low.iloc[i:i+wind].idxmin())
        for i in range(candleid-r1, candleid+1, wind):
            maxim = np.append(maxim, df.High.loc[i:i+wind].max())
            xxmax = np.append(xxmax, df.High.iloc[i:i+wind].idxmax())
        slmin, intercmin = np.polyfit(xxmin, minim,1)
        slmax, intercmax = np.polyfit(xxmax, maxim,1)
        
        if(abs(slmin-slmax)<sldiff):
            sldiff = abs(slmin-slmax)
            optbackcandles=r1
            slminopt = slmin
            slmaxopt = slmax
            intercminopt = intercmin
            intercmaxopt = intercmax
            maximopt = maxim.copy()
            minimopt = minim.copy()
            xxminopt = xxmin.copy()
            xxmaxopt = xxmax.copy()



    adjintercmax = (df.High.iloc[xxmaxopt] - slmaxopt*xxmaxopt).max()
    adjintercmin = (df.Low.iloc[xxminopt] - slminopt*xxminopt).min()
    return xxminopt,slminopt*xxminopt + adjintercmin,xxmaxopt, slmaxopt*xxmaxopt + adjintercmax
# def channel(df,last):
#     # df=df[df['Volume']!=0]
#     # df.reset_index(drop=True, inplace=True)
#     return find(df,last)