import requests
import csv
from selenium import webdriver
from time import sleep
from datetime import datetime
from matplotlib import pyplot as plt

def BTC():
    URL = 'https://lightning.bitflyer.jp/v1/getticker?product_code=FX_BTC_JPY'
    ticker = requests.get(URL).json()
    price = int(ticker['ltp'])
    return price

def VOL():
    for buyvol in driver.find_elements_by_id("buyVolumePerMeasurementTime"):
        buy = buyvol.text
    for sellvol in driver.find_elements_by_id("sellVolumePerMeasurementTime"):
        sell = sellvol.text
    return buy,sell

driver = webdriver.PhantomJS()
driver.get("https://inagoflyer.appspot.com/btcmac")

while True:
    btc = BTC()
    vol = VOL()
    print('-----------------------------')
    text = 'price: ' + str(btc) + '\n' + 'buyVol: ' + vol[0] + '\n' + 'sellVol: ' + vol[1]
    print(datetime.now())
    print(text)
    with open('log.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([datetime.now(), btc, vol[0], vol[1]])
    sleep(1)
