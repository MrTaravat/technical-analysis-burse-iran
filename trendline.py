import trendln
import pandas as pd

def trendline(data,maxCandle=100):
    if len(data) >= maxCandle:
        data=data[-maxCandle:].reset_index()
    mins,maxs = trendln.calc_support_resistance( (data.Low, data.High),accuracy=8)
    (minimaIdxs, pmin, mintrend, minwindows), (maximaIdxs, pmax, maxtrend, maxwindows) = mins, maxs
    support=[]
    for i in mintrend:
        support.append([i[0][0],i[0][-1]])
        if(len(support)==4):
            break
    resistance=[]
    for i in maxtrend:
        resistance.append([i[0][0],i[0][-1]])  
        if(len(resistance)==4):
            break
    print(maximaIdxs,'\n\n\n\n\n', pmax, '\n\n\n\n\n',maxtrend, '\n\n\n\n\n',maxwindows)
    return support,resistance