from fcoin import Fcoin
import json,time

fcoin = Fcoin()
ftusdt = fcoin.get_market_ticker('ftusdt')['data']['ticker']
print("%.4f" % ftusdt[0])

