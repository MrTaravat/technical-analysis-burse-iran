from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import glob
import os
import shutil
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

def geturl():
    global list_url,list_name,list_label,lenlist
    list_url=[]
    list_name=[]
    list_label=[]
    url="http://www.tsetmc.com/Loader.aspx?ParTree=111C1417" 
    response=requests.get(url)      
    soup = BeautifulSoup(response.content,"html.parser")

    for a_href in soup.find_all("a", href=True):
        if(a_href["href"].split("=")[-1] in list_url):
            list_name.append(a_href.text)
        else:
            list_label.append(a_href.text)
            list_url.append(a_href["href"].split("=")[-1])
    lenlist=len(list_url)
  
def start_scraping_download():
    global data
    data=[]
    for url in range(1,lenlist):
        in_data=[]
        link= 'http://www.tsetmc.com/tsev2/data/Export-txt.aspx?t=i&a=1&b=0&i=' + list_url[url]
        in_data.append(list_name[url])
        in_data.append(list_label[url])
        in_data.append(list_url[url])
        data.append(in_data)
        content=requests.get(link)
        with open('temp/'+list_label[url]+'.csv', 'w') as f:
            writer = csv.writer(f)
            for line in content.iter_lines():
                writer.writerow(line.decode('utf-8').split(','))
        time.sleep(0.03)

def list_csv():
    header = ['name','label','link']
    with open('/home/mrtaravat/Desktop/project/list/list.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
def sortAndChangeColumns():
    for name in os.listdir("/home/mrtaravat/Desktop/project/temp/"):
        if not name.startswith('.'):  #hidden file
            dataFrame = pd.read_csv("/home/mrtaravat/Desktop/project/temp/"+name) 
            correct_df = dataFrame.copy()
            correct_df.rename(columns={'<TICKER>': 'Name', '<DTYYYYMMDD>': 'Date','<FIRST>': 'First','<HIGH>': 'High','<LOW>': 'Low','<CLOSE>': 'Close', '<VALUE>': 'Value','<VOL>': 'Volume','<OPENINT>': 'Openint','<PER>': 'Per','<OPEN>': 'Open', '<LAST>': 'Last'}, inplace=True)
            correct_df.to_csv('burse/'+name, index=False,header=True)
            dataFrame = pd.read_csv('burse/'+name)
            dataFrame.sort_values(["Date"],axis=0, ascending=True,inplace=True,na_position='first')
            dataFrame.to_csv('burse/'+name, index=False,header=True)
def init():
    geturl()
    start_scraping_download()
    list_csv()
    sortAndChangeColumns()
    try:
        shutil.rmtree('temp')
        print("% s removed successfully")
    except OSError as error:
        print(error)
        print("File path can not be removed")