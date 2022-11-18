import  streamlit as  st
import matplotlib.pyplot as plt
import pandas as pd
import sup_res_finder as sr
import Charts
import indicators
import machine
import data_mining_tsetmc
global symbol
import pandas as pd

st.write('''
# نمودار سهام
''')

def sidebar():
    global AroonSelect,BollingerBandsSelect,RsiSelect,EmaSelect,MacdSelect,AlligatorSelect,Support_Resistance,TrendLine,maxcandle,Triangle,Channel,ChannelLast
    maxcandle= 100
    ChannelLast= 100
    AroonSelect=st.sidebar.checkbox('Aroon')
    BollingerBandsSelect=st.sidebar.checkbox('BollingerBands')
    RsiSelect=st.sidebar.checkbox('Rsi')
    EmaSelect=st.sidebar.checkbox('Ema')
    MacdSelect=st.sidebar.checkbox('macd')
    AlligatorSelect=st.sidebar.checkbox('alligator')
    Support_Resistance=st.sidebar.checkbox('support resistance')
    TrendLine=st.sidebar.checkbox('TrendLine')
    if TrendLine==True:
        maxcandle=st.sidebar.text_input("بر روی چند کندل اخر محاسابت را انجام دهد")
    Triangle=st.sidebar.checkbox('triangle')
    Channel=st.sidebar.checkbox('Channel')
    if Channel==True:
        ChannelLast=st.sidebar.text_input("بر روی چند کندل اخر محاسابت را انجام دهد")
def get_select():
    global option,listCompany
    listCompany=pd.read_csv('list/list.csv')
    option = st.selectbox(
     'سهم مورد نظر',
     (listCompany['label']))
    return option
    

def get_selectData(symbol):
    selectData=pd.read_csv('/home/mrtaravat/Desktop/project/burse/'+symbol+'.csv')  
    
    return selectData

def lineChart(dataCsv):
    if not('/' in str(dataCsv['Date'].values[1])):
        dataCsv['Date'] = pd.to_datetime(dataCsv['Date'], format='%Y%m%d')
    dataCsv=dataCsv.set_index(pd.DatetimeIndex(dataCsv['Date']))
    st.header(' Close Price\n')
    st.line_chart(dataCsv['Last'])
    
def writeSignal(dataCsv):
    if AroonSelect==True:
        st.markdown(indicators.Aroon(dataCsv),unsafe_allow_html=True)
    if BollingerBandsSelect==True:
        st.markdown(indicators.BollingerBands(dataCsv),unsafe_allow_html=True)
    if RsiSelect==True:
        st.markdown(indicators.Rsi(dataCsv),unsafe_allow_html=True)
    if EmaSelect==True:
        st.markdown(indicators.Ema(dataCsv),unsafe_allow_html=True)
    if MacdSelect==True:
        st.markdown(indicators.Macd(dataCsv),unsafe_allow_html=True)
    if AlligatorSelect==True:
        st.markdown(indicators.Alligator(dataCsv),unsafe_allow_html=True)
    

def init():
    sidebar()
    if st.button('آپدیت داده ها'):
        data_mining_tsetmc.init()
    symbol = get_select()
    selectData=get_selectData(symbol)
    if st.button('CandelStick chart and indicators'):
        Charts.drawChart(selectData,AroonSelect,BollingerBandsSelect,RsiSelect,EmaSelect,MacdSelect,AlligatorSelect,Support_Resistance,TrendLine,int(maxcandle),Triangle,Channel,int(ChannelLast))
    writeSignal(selectData)
    lineChart(selectData)
    if st.button('پیشبینی قیمت با ماشین لرنینگ'):
        AccuracySvr,PredictionSvr=machine.ML_SVR(selectData, 5)
        st.header('SVR Accuracy')
        st.success(AccuracySvr)
        st.header('SVR Prediction')
        st.success(PredictionSvr)
        AccuracyLr,PredictionLr=machine.ML_LR(selectData, 5)
        st.header('LR Accuracy')
        st.success(AccuracyLr)
        st.header('LR Prediction')
        st.success(PredictionLr)
    
init()