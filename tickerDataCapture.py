#!/usr/bin/env python3

'''
This script:
Gets ticker information from poloniex in the following format:
{'id': 148, 'last': 0.10399494, 'lowestAsk': 0.10399488, 'highestBid': 0.10392402, 'percentChange': 0.08324767, 'baseVolume': 4393.20335889, 'quoteVolume': 43522.76987116, 'isFrozen': 0, 'high24hr': 0.10515, 'low24hr': 0.09566}
It then adds the date & time data to the ticker dictionary
Then inserts the information dictionary into the mongodb

'''

###################
# DEBUG ON OR OFF #
debug = 0 #########
# 1 = ON, 0 = OFF #
###################


# Import all dependencies #
###########################
import pymongo
from pymongo import MongoClient
from logins import mongodburl
from config import tradepair
import pprint
import json
import datetime
from poloniex import Poloniex
import numpy as np


# Set up the database to use globally #
#######################################
client = pymongo.MongoClient(mongodburl)
db = client.CryptoTrader

'''

### Code Starts Here ###

'''

def main():

    # Print out original databse #
    ##############################
    if debug == 1:
        print('------------------------------------------DEBUG')
        print('Check whats in the database to start with: ')
        for a in db.tickerdata.find():
            pprint.pprint(a)


    # Get the ticker from Poloniex #
    ################################
    polo = Poloniex() # Keep this in here so the python script closes
    ticker = dict(polo.returnTicker()[tradepair])
    if debug == 1:
        print('------------------------------------------DEBUG')
        print('Check ticker has been captured: ')
        print(ticker)


    # Adds time and date to ticker dict #
    #####################################
    now = datetime.datetime.now()
    ticker['timeanddate'] = str(np.datetime64('now'))
    if debug == 1:
        print('------------------------------------------DEBUG')
        print('Check Time has been added to ticker: ')
        print(ticker)


    # Adds data to the mongodb #
    ############################
    _id = db.tickerdata.insert(ticker)
    if debug == 1:
        print('------------------------------------------DEBUG')
        print('Check whats in the database: ')
        for a in db.tickerdata.find():
            pprint.pprint(a)
    print(_id)
    return(_id)

'''

### EXECUTE THE SCRIPT ###

'''

if __name__ == "__main__":
    main()
