from select import select
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import indicators
import pandas as pd
import sup_res_finder
import trendline 
import TrianglePatterns
import ChannelsDetection
def checkSelectForDraw(Aroon,Rsi,Macd):
    selected=['Chart']
    intRow=1
    row_height=[0.5]
    if(Aroon==True):
        selected.append('Aroon')
        intRow+=1
        row_height.append(0.15)
    if(Rsi==True):
        selected.append('Rsi')
        intRow+=1
        row_height.append(0.15)
    if(Macd==True):
        selected.append('Macd')
        intRow+=1
        row_height.append(0.15)
    return intRow,tuple(selected),row_height
def CandlestickChart(fig,dataCsv):
    candlestick= go.Candlestick(x=dataCsv.index,open=dataCsv['First'],high=dataCsv['High'],low=dataCsv['Low'],close=dataCsv['Last'])
    fig.add_trace(candlestick,row=1,col=1)
    
def AroonChart(fig,dataCsv):
    AroonUp,AroonDown=indicators.AroonChart(dataCsv)
    fig.add_trace(AroonDown,row=2,col=1)
    fig.add_trace(AroonUp,row=2,col=1)

def BollingerBandsChart(fig,dataCsv):
    upperband, middleband, lowerband=indicators.BollingerBandsChart(dataCsv)
    macd, macdsignal, macdhist=indicators.MacdChart(dataCsv)
    fig.add_trace(upperband,row=1,col=1)
    fig.add_trace(middleband,row=1,col=1)
    fig.add_trace(lowerband,row=1,col=1)

def RsiChart(fig,dataCsv):
    rsi=indicators.RsiChart(dataCsv)
    fig.add_trace(rsi,row=3,col=1)
def EmaChart(fig,dataCsv):
    ema=indicators.EmaChart(dataCsv)
    fig.add_trace(ema,row=1,col=1)
def MacdChart(fig,dataCsv):
    macd, macdsignal, macdhist=indicators.MacdChart(dataCsv)
    fig.add_trace(macdsignal,row=4,col=1)
    fig.add_trace(macd,row=4,col=1)
    fig.add_trace(macdhist,row=4,col=1)
def alligatorChart(fig,dataCsv,selectData):
    alligator_teeth, alligator_lips, alligator_jaw=indicators.AlligatorChart(selectData)
    fig.add_trace(go.Scatter(x=dataCsv.index,
    y=alligator_teeth,
    name = 'alligator_teeth', # Style name/legend entry with html tags
    connectgaps=True # override default to connect the gaps
    ),row=1,col=1)
    fig.add_trace(go.Scatter(x=dataCsv.index,
    y=alligator_lips,
    name = 'alligator_lips', # Style name/legend entry with html tags
    connectgaps=True # override default to connect the gaps
    ),row=1,col=1)
    fig.add_trace(go.Scatter(x=dataCsv.index,
    y=alligator_jaw,
    name = 'alligator_jaw', # Style name/legend entry with html tags
    connectgaps=True # override default to connect the gaps
    ),row=1,col=1)
def Support_ResistanceChart(fig,dataCsv):
    ob_Support_Resistance=sup_res_finder.Sup_Res_Finder()
    results=ob_Support_Resistance.find_levels(dataCsv)
    for result in results[-20:]:

        fig.add_trace(go.Scatter(x=[dataCsv.index[result[0]],( dataCsv.index[result[0]+300 if (result[0]+300)<len(dataCsv.index) else len(dataCsv.index)-1])], y=[result[1],result[1]] ,name='sup_res',line_color='#000000' ), row=1, col=1)

def TrendLineChart(fig,dataCsv,selectData,maxcandle):
    TL_support,TL_resistances=trendline.trendline(selectData,maxcandle)
    for su in TL_support:
        fig.add_trace(go.Scatter(
            x=[dataCsv.index[-(maxcandle-su[0])],dataCsv.index[-(maxcandle-su[1])]],y=[dataCsv['Low'].values[-(maxcandle-su[0])],dataCsv['Low'].values[-(maxcandle-su[1])]], name='trendline support',line_color='#00FF00' ), row=1, col=1)#
        
    for re in TL_resistances:
        fig.add_trace(go.Scatter(
            x=[dataCsv.index[-(maxcandle-re[0])],dataCsv.index[-(maxcandle-re[1])]],y=[dataCsv['High'].values[-(maxcandle-re[0])],dataCsv['High'].values[-(maxcandle-re[1])]], name='trendline resistances',line_color='#EE4B2B' ), row=1, col=1)#
        
def TriangleChart(fig,dataCsv,selectData):
    pos=TrianglePatterns.Triangle(selectData)
    if pos!=-1:
        fig.add_trace(go.Scatter(x=[dataCsv.index[pos[0][0][0]],dataCsv.index[pos[0][0][-1]]], y=[pos[0][1][0],pos[0][1][-1]], mode='lines', name='Triangle min slope',line_color='#00FF00'), row=1, col=1)
        
        fig.add_trace(go.Scatter(x=[dataCsv.index[pos[1][0][0]],dataCsv.index[pos[1][0][-1]]], y=[pos[1][1][0],pos[1][1][-1]], mode='lines', name='Triangle max slope',line_color='#ff0000'), row=1, col=1)
def ChannelBandsChart(fig,dataCsv,selectData,ChannelLast):
    minx,miny,maxx,maxy=ChannelsDetection.find(selectData,ChannelLast)
    fig.add_trace(go.Scatter(x=[dataCsv.index[minx[0]],dataCsv.index[minx[-1]]], y=[miny[0],miny[-1]], mode='lines', name='Channel min ',line_color='#00FF00'), row=1, col=1)
    
    fig.add_trace(go.Scatter(x=[dataCsv.index[maxx[0]],dataCsv.index[maxx[-1]]], y=[maxy[0],maxy[-1]], mode='lines', name='Channel max ',line_color='#ff0000'), row=1, col=1)


def drawChart(selectData,Aroon,BollingerBands,Rsi,Ema,Macd,Alligator,Support_Resistance,TrendLine,maxcandle,Triangle,Channel,ChannelLast):
    
    intRow,title,row_height=checkSelectForDraw(Aroon,Rsi,Macd)
    dataCsv=selectData
    if not('/' in str(dataCsv['Date'].values[1])):
        dataCsv['Date'] = pd.to_datetime(dataCsv['Date'], format='%Y%m%d')
    dataCsv=dataCsv.set_index(pd.DatetimeIndex(dataCsv['Date']))
    fig=make_subplots(rows=intRow,cols=1,shared_xaxes=True,vertical_spacing=0.03,subplot_titles=title,row_heights=row_height)
    
    CandlestickChart(fig,dataCsv)
    
    if Aroon==True:
        AroonChart(fig,dataCsv)
    if BollingerBands==True:
        BollingerBandsChart(fig,dataCsv)
    if Rsi==True:
        RsiChart(fig,dataCsv)
    if Ema==True:
        EmaChart(fig,dataCsv)
    if Macd==True:
        MacdChart(fig,dataCsv)
    if Alligator==True:
        alligatorChart(fig,dataCsv,selectData)
    if Support_Resistance==True:
        Support_ResistanceChart(fig,dataCsv)
    if TrendLine==True:
        TrendLineChart(fig,dataCsv,selectData,maxcandle)
    if Triangle ==True:
        TriangleChart(fig,dataCsv,selectData)
    if Channel==True:
        ChannelBandsChart(fig,dataCsv,selectData,ChannelLast)
        
    fig['layout'].update(height=1400, width=1800,)
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.show()
