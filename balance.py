from fcoin import Fcoin
import json,time


def trunc(f, n):
        sarr = str(f).split('.')    
        if len(sarr) == 2:
            s1, s2 = str(f).split('.')
        else:
            s1 = str(f)
            s2 = '0'
        if n == 0:
            return s1
        if n <= len(s2):
            return s1 + '.' + s2[:n]
        return s1 + '.' + s2 + '0' * (n - len(s2))


currency = {'ft':'usdt','btc':'usdt','eth':'usdt','bch':'usdt','ltc':'usdt','etc':'usdt','btm':'usdt','zip':'eth','icx':'eth','omg':'eth','zil':'eth'}

fcoin = Fcoin()
fcoin.auth('key', 'secret')

#try:

# balances
balance = fcoin.get_balance()['data']
balances = [bal for bal in balance if bal['balance'] != '0.000000000000000000']

if balances:
	sum_usdt = 0
	for bal in balances:
		if bal['currency'] != 'usdt':
			tickername = bal['currency']+currency[bal['currency']]
			ticker = fcoin.get_market_ticker(tickername)['data']['ticker']
			
			balance_usdt = float(bal['balance'])*ticker[0]
			if currency[bal['currency']] != 'usdt':
				tickername = currency[bal['currency']]+currency[currency[bal['currency']]]
				ticker = fcoin.get_market_ticker(tickername)['data']['ticker']
				balance_usdt = balance_usdt*ticker[0]

			sum_usdt += balance_usdt
			print("{}	{}	${}	{}	{}".format(bal['currency'].upper() , trunc(bal['balance'],4), trunc(balance_usdt,2), tickername.upper() , trunc(ticker[0],4)))
	
	print("TOTAL		${}".format(trunc(sum_usdt,2)))

#except:
	#print "Oops! Try again..."


