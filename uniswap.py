from sgqlc.endpoint.http import HTTPEndpoint
import json
import time
import requests

############################
# send message
# you have to replace <receiver_id> with id of telegram user
# replace <BOT_TOKEN> with your bot token
############################
def sendMessage(message):
	receiver = '<receiver_id>'
	baseUrl = 'https://api.telegram.org/bot<BOT_TOKEN>/sendMessage?chat_id={}&text="{}"'.format(receiver, message)
	requests.get(baseUrl)

############################
# retun token data by number
############################
def tokenData(number):
	number = str(number - 1)
	query = "{  tokens(first: 1, skip: "
	query = query + number + ") {     id     name     symbol  }}"
	endpoint = HTTPEndpoint(url='https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2')
	result = endpoint(query=query)
	result = result['data']
	result = result['tokens']
	try:
		tokenData = result[0]
		return tokenData
	except:
		return None

###########################
# check if id exists
###########################
def checkId(tokenId):
	if tokenId != None:
		return True
	else:
		return False

############################
# returns token name
############################
def getTokenName(tokenData):
	if tokenData != None:
		tokenName = tokenData['name']
		return tokenName
	else:
		return None

############################
# returns token symbol
############################
def getTokenSymbol(tokenData):
	if tokenData != None:
		tokenSymbol = tokenData['symbol']
		return tokenSymbol
	else:
		return None

###########################
# return token data
###########################
def getTokenId(tokenData):
	if tokenData != None:
		tokenId = tokenData['id']
		return tokenData
	else:
		return None

############################
## PROGRAM DATA
############################
tokenNumber = 23686
sleepHours = 1
sleep = sleepHours * 3600

###########################
### PROGRAM LOGIC
###########################
while True:
	name = getTokenName(tokenData(tokenNumber))
	symbol = getTokenSymbol(tokenData(tokenNumber))
	if checkId(getTokenId(tokenData(tokenNumber))):
		message = "We have new token on UNISAWP\n Name: {}\n Symbol: {}".format(name, symbol)
		print("we have token with number: " + str(tokenNumber))
		sendMessage(message)
		tokenNumber = tokenNumber + 1
		time.sleep(sleep)
	else:
		print('token is not exist')
