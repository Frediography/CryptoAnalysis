# CryptoAnalysis 

A small tool that takes information out of Poloniex and puts it into MongoDB

There is also a small tool here that takes information out ot twitter using Tweepy and analysis the sentiment. 

Finally - there is a Jupyter notebook that uses this information to see if there is any correllation between the two.

There is no correlation I could find.

You will need to create a logins.py and a config.py.

# Thanks to
- Thanks to https://github.com/tweepy/tweepy (Tweepy), for the twitter bits 
- Thanks to poloniex for their awesome API
- Thanks to https://github.com/s4w3d0ff/python-poloniex for the poloniex api wrapper 

## logins.py
'''python
#LOGIN DOC:
#* Twitter API Keys
#* Poloniex API Keys
#* MongoDB URL

#Twitter consumer key, consumer secret, access token, access secret
ckey=""
csecret=""
atoken=""
asecret=""

#Poloniex API stuff - not required if you're just taking information from them
POLONIEX_API_KEY = "abc"
POLONIEX_API_SECRET = "123"
SENDER_EMAIL_ADDRESS = "joe@gmail.com"
BACKUP_EMAIL_ADDRESS = "bob@gmail.com"

#Mongo DB URL etc.
# Use below for the mongodb as a service as well as if you've set it up locally
mongodburl = "mongodb://localhost:27017"
'''


## config.py
'''python
#CONFIG DOCUMENT
#* tradepair in poloniex format
#* MongoDB datbase collection

# Crypto Pair to Trade
tradepair = 'USDT_ETH'
# the collection within the mongodb that you're using
databasecollection = 'testcollection'
'''
