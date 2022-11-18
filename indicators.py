import talib as ta
import plotly.graph_objects as go
from tapy import Indicators
import jdatetime
def Aroon(dataCsv):
    aroondown, aroonup = ta.AROON(dataCsv['High'].values, dataCsv['Low'].values, timeperiod=14)
    if aroondown[-1]<aroonup[-1] and aroondown[-2]>aroonup[-2]:
        return '<h5 style="color:green">Aroon signal buy</h5>'
    elif aroondown[-1]>aroonup[-1] and aroondown[-2]<aroonup[-2]:
        return '<h5 style="color:red">Aroon signal sell</h5>'
    else:
        return '<h5 style="color:blue">Aroon not signal for now</h5>'

def AroonBackTest(dataCsv): 
    aroondown, aroonup = ta.AROON(dataCsv['High'].values, dataCsv['Low'].values, timeperiod=14)
    for i in range(0,len(aroonup)):
        if aroondown[i]<aroonup[i] and aroondown[i-1]>aroonup[i-1]:
            date=str(dataCsv['Date'][i])
            print('buy   '+jdatetime.datetime.fromgregorian(day=int(date[6:8]),month=int(date[4:6]),year=int(date[:4])).strftime('%Y-%m-%d'))
        elif aroondown[i]>aroonup[i] and aroondown[i-1]<aroonup[i-1]:
            date=str(dataCsv['Date'][i])
            print('sell   '+jdatetime.datetime.fromgregorian(day=int(date[6:8]),month=int(date[4:6]),year=int(date[:4])).strftime('%Y-%m-%d'))

def AroonChart(dataCsv):

    aroondown, aroonup = ta.AROON(dataCsv['High'].values, dataCsv['Low'].values, timeperiod=14)
    return go.Scatter(
        y=aroonup,
        name = 'aroonup', # Style name/legend entry with html tags
        connectgaps=True # override default to connect the gaps
    ),go.Scatter(
        y=aroondown,
        name='aroondown',
    connectgaps=True)

def BollingerBands(dataCsv):
    upperband, middleband, lowerband = ta.BBANDS(dataCsv['Last'].values, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    if (  lowerband[-1]-(lowerband[-1]*0.016)<= dataCsv['First'].values[-1] <=lowerband[-1]+(lowerband[-1]*0.016)) and (( dataCsv['Last'].values[-1]>dataCsv['First'].values[-1]) or ((dataCsv['Last'].values[-1]-dataCsv['First'].values[-1])<0.01*dataCsv['Last'].values[-1])):
        return '<h5 style="color:green">BollingerBands signal buy</h5>'
    elif ( upperband[-1]+(upperband[-1]*0.016)>= dataCsv['First'].values[-1] >=upperband[-1]-(upperband[-1]*0.016) ) and (( dataCsv['Last'].values[-1]<dataCsv['First'].values[-1]) or ((dataCsv['Last'].values[-1]-dataCsv['First'].values[-1])<0.01*dataCsv['Last'].values[-1])):
        return '<h5 style="color:red">BollingerBands signal sell</h5>'
    else:
        return '<h5 style="color:blue">BollingerBands not signal for now</h5>'
    
   
def BollingerBandsBackTest(dataCsv):
    upperband, middleband, lowerband = ta.BBANDS(dataCsv['Last'].values, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    for i in range(0,len(dataCsv.index)):
        if (  lowerband[i]-(lowerband[i]*0.016)<= dataCsv['First'].values[i] <=lowerband[i]+(lowerband[i]*0.016)) and (( dataCsv['Last'].values[i]>dataCsv['First'].values[i]) or ((dataCsv['Last'].values[i]-dataCsv['First'].values[i])<0.01*dataCsv['Last'].values[i])):
            date=str(dataCsv['Date'][i])
            print('buy   '+jdatetime.datetime.fromgregorian(day=int(date[6:8]),month=int(date[4:6]),year=int(date[:4])).strftime('%Y-%m-%d')+"       Last+"+str(dataCsv['Last'].values[i])+'    First'+str(dataCsv['First'].values[i]))
        elif ( upperband[i]+(upperband[i]*0.016)>= dataCsv['First'].values[i] >=upperband[i]-(upperband[i]*0.016) ) and (( dataCsv['Last'].values[i]<dataCsv['First'].values[i]) or ((dataCsv['Last'].values[i]-dataCsv['First'].values[i])<0.01*dataCsv['Last'].values[i])):
            date=str(dataCsv['Date'][i])
            print('sell   '+jdatetime.datetime.fromgregorian(day=int(date[6:8]),month=int(date[4:6]),year=int(date[:4])).strftime('%Y-%m-%d')+"       Last+"+str(dataCsv['Last'].values[i])+'    First'+str(dataCsv['First'].values[i]))

def BollingerBandsChart(dataCsv):
    upperband, middleband, lowerband = ta.BBANDS(dataCsv['Last'].values, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    return go.Scatter(x=dataCsv.index,
        y=upperband,
        name = 'upperband', # Style name/legend entry with html tags
        connectgaps=True # override default to connect the gaps
    ),go.Scatter(x=dataCsv.index,
        y=middleband,
        name='middleband',
    connectgaps=True),go.Scatter(x=dataCsv.index,
        y=lowerband,
        name='lowerband',
    connectgaps=True)
def Rsi(dataCsv):
    rsi = ta.RSI(dataCsv['Last'].values, timeperiod=14)
    if rsi[-1]>=30 and rsi[-2]<30:
        return '<h5 style="color:green">RSI signal buy</h5>'
    elif rsi[-1]<=70 and rsi[-2]>70:
        return '<h5 style="color:red">RSI signal sell</h5>'
    else:
        return '<h5 style="color:blue">RSI not signal for now</h5>'
def RsiBackTest(dataCsv):
    rsi = ta.RSI(dataCsv['Last'].values, timeperiod=14)
    for i in range(0,len(rsi)):
        if rsi[i]>=30 and rsi[i-1]<30:
            date=str(dataCsv['Date'][i])
            print('buy   '+jdatetime.datetime.fromgregorian(day=int(date[6:8]),month=int(date[4:6]),year=int(date[:4])).strftime('%Y-%m-%d'))
        elif rsi[i]<=70 and rsi[i-1]>70:
            date=str(dataCsv['Date'][i])
            print('sell   '+jdatetime.datetime.fromgregorian(day=int(date[6:8]),month=int(date[4:6]),year=int(date[:4])).strftime('%Y-%m-%d'))

def RsiChart(dataCsv):
    rsi = ta.RSI(dataCsv['Last'].values, timeperiod=14)
    return go.Scatter(x=dataCsv.index,
        y=rsi,
        name = 'rsi', # Style name/legend entry with html tags
        connectgaps=True # override default to connect the gaps
    )
def Ema(dataCsv):
    ema = ta.EMA(dataCsv['Last'].values, timeperiod=9)
    if ema[-1]<=dataCsv['Last'].values[-1] and ema[-2]>=dataCsv['Last'].values[-2] and dataCsv['Last'].values[-1]>dataCsv['First'].values[-1]:
        return '<h5 style="color:green">EMA signal buy</h5>'
    elif ema[-1]>=dataCsv['Last'].values[-1] and ema[-2]<=dataCsv['Last'].values[-2] and dataCsv['Last'].values[-1]<dataCsv['First'].values[-1]:
        return '<h5 style="color:red">EMA signal sell</h5>'
    else:
        return '<h5 style="color:blue">EMA not signal for now</h5>'

def EmaBackTest(dataCsv):
    ema = ta.EMA(dataCsv['Last'].values, timeperiod=9)
    for i in range(0,len(ema)):
        if ema[i]<=dataCsv['Last'].values[i] and ema[i-1]>=dataCsv['Last'].values[i-1] and dataCsv['Last'].values[i]>dataCsv['First'].values[i]:
            date=str(dataCsv['Date'][i])
            print('buy   '+jdatetime.datetime.fromgregorian(day=int(date[6:8]),month=int(date[4:6]),year=int(date[:4])).strftime('%Y-%m-%d'))
        elif ema[i]>=dataCsv['Last'].values[i] and ema[i-1]<=dataCsv['Last'].values[i-1] and dataCsv['Last'].values[i]<dataCsv['First'].values[i]:
            date=str(dataCsv['Date'][i])
            print('sell   '+jdatetime.datetime.fromgregorian(day=int(date[6:8]),month=int(date[4:6]),year=int(date[:4])).strftime('%Y-%m-%d'))

def EmaChart(dataCsv):
    ema = ta.EMA(dataCsv['Last'].values, timeperiod=14)
    return go.Scatter(x=dataCsv.index,
        y=ema,
        name = 'ema', # Style name/legend entry with html tags
        connectgaps=True # override default to connect the gaps
    )

def Macd(dataCsv):
    macd, macdsignal, macdhist = ta.MACD(dataCsv['Last'].values, fastperiod=12, slowperiod=26, signalperiod=9)
    if macd[-1]>=macdsignal[-1] and macd[-2]<macdsignal[-2]:
        return '<h5 style="color:green">MACD signal buy</h5>'
    elif macd[-1]<=macdsignal[-1] and macd[-2]>macdsignal[-2]:
        return '<h5 style="color:red">MACD signal sell</h5>'
    else:
        return '<h5 style="color:blue">MACD not signal for now</h5>'

def MacdBackTest(dataCsv):
    macd, macdsignal, macdhist = ta.MACD(dataCsv['Last'].values, fastperiod=12, slowperiod=26, signalperiod=9)
    for i in range(0,len(macd)):
        if macd[i]>=macdsignal[i] and macd[i-1]<macdsignal[i-1]:
            date=str(dataCsv['Date'][i])
            print('buy   '+jdatetime.datetime.fromgregorian(day=int(date[6:8]),month=int(date[4:6]),year=int(date[:4])).strftime('%Y-%m-%d'))
        elif macd[i]<=macdsignal[i] and macd[i-1]>macdsignal[i-1]:
            date=str(dataCsv['Date'][i])
            print('sell   '+jdatetime.datetime.fromgregorian(day=int(date[6:8]),month=int(date[4:6]),year=int(date[:4])).strftime('%Y-%m-%d'))

def MacdChart(dataCsv):
    macd, macdsignal, macdhist = ta.MACD(dataCsv['Last'].values, fastperiod=12, slowperiod=26, signalperiod=9)
    return go.Scatter(
        y=macd,
        name = 'macd', # Style name/legend entry with html tags
        connectgaps=True # override default to connect the gaps
    ),go.Scatter(
        y=macdsignal,
        name='macdsignal',
    connectgaps=True),go.Scatter(
        y=macdhist,
        name='macdhist',
    connectgaps=True)
def Alligator(dataCsv):
    indcator=Indicators(dataCsv)
    indcator.alligator(period_jaws=13, period_teeth=8, period_lips=5, shift_jaws=8, shift_teeth=5, shift_lips=3, column_name_jaws='alligator_jaw', column_name_teeth='alligator_teeth', column_name_lips='alligator_lips')
    if indcator.df['alligator_teeth'].values[-1]<indcator.df['alligator_lips'].values[-1] and indcator.df['alligator_teeth'].values[-2]>= indcator.df['alligator_lips'].values[-2]:
        return '<h5 style="color:green">Alligator signal buy</h5>'
    elif indcator.df['alligator_teeth'].values[-1]>indcator.df['alligator_lips'].values[-1] and indcator.df['alligator_teeth'].values[-2]<= indcator.df['alligator_lips'].values[-2]:
        return '<h5 style="color:red">Alligator signal buy</h5>'
    else:
        return '<h5 style="color:blue">Alligator not signal for now</h5>'
def AlligatorBackTest(dataCsv):
    indcator=Indicators(dataCsv)
    indcator.alligator(period_jaws=21, period_teeth=13, period_lips=8, shift_jaws=8, shift_teeth=5, shift_lips=3, column_name_jaws='alligator_jaw', column_name_teeth='alligator_teeth', column_name_lips='alligator_lips')
    for i in range(0, len(indcator.df['alligator_teeth'])) :
        if indcator.df['alligator_teeth'].values[i] < indcator.df['alligator_lips'].values[i] and indcator.df['alligator_teeth'].values[i-1]>= indcator.df['alligator_lips'].values[i-1]:
            date=str(dataCsv['Date'][i])
            print('Alligator signal buy       '+jdatetime.datetime.fromgregorian(day=int(date[6:8]),month=int(date[4:6]),year=int(date[:4])).strftime('%Y-%m-%d'))
        elif indcator.df['alligator_teeth'].values[i]>indcator.df['alligator_lips'].values[i] and indcator.df['alligator_teeth'].values[i-1]<= indcator.df['alligator_lips'].values[i-1]:
            date=str(dataCsv['Date'][i])
            print('Alligator signal sell       '+jdatetime.datetime.fromgregorian(day=int(date[6:8]),month=int(date[4:6]),year=int(date[:4])).strftime('%Y-%m-%d'))

def AlligatorChart(dataCsv):
    indcator=Indicators(dataCsv)
    indcator.alligator(period_jaws=13, period_teeth=8, period_lips=5, shift_jaws=8, shift_teeth=5, shift_lips=3, column_name_jaws='alligator_jaw', column_name_teeth='alligator_teeth', column_name_lips='alligator_lips')
  
    return indcator.df['alligator_teeth'].values,indcator.df['alligator_lips'].values,indcator.df['alligator_jaw'].values