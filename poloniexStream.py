from poloniex import Poloniex
import json
polo = Poloniex()

# json_string =  '{ "id":"John", "age":30, "car":null }'
#print(polo.returnTicker()['BTC_ETH'])
json_string = {'id': 148, 'last': 0.10399494, 'lowestAsk': 0.10399488, 'highestBid': 0.10392402, 'percentChange': 0.08324767, 'baseVolume': 4393.20335889, 'quoteVolume': 43522.76987116, 'isFrozen': 0, 'high24hr': 0.10515, 'low24hr': 0.09566}


print(json_string)
parsed_json = json.loads(json_string)
print(parsed_json['id'])
