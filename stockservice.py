import time
from flask import Flask , request, jsonify
from flask_caching import Cache
from stock import Stock

app = Flask(__name__)

cacheConfig = {
'CACHE_TYPE':'filesystem',
'CACHE_DIR':'.',
'CACHE_DEFAULT_TIMEOUT':10800,
'CACHE_THRESHOLD': 922337203684778

}

cache = Cache(app, config = cacheConfig)

def storeStockData():
    stockDic = {}
    stockDic['TEA'] = Stock('TEA','Common',0,None,100)
    stockDic['POP'] = Stock('POP','Common',8,None,100)
    stockDic['ALE'] = Stock('ALE','Common',23,None,100)
    stockDic['GIN'] = Stock('GIN','Preferred',8,2,100)
    stockDic['JOE'] = Stock('JOE','Common',13,None,250)
    cache.set('stocks',stockDic, timeout=10800)

def storeSampleTradesData():
    currentTime = int(time.time())
    tradesList = []
    tradesList.append(['TEA',currentTime,100,'Buy',2563])
    tradesList.append(['JOE',currentTime,75,'Sell',968])
    tradesList.append(['GIN',currentTime,200,'Buy',8659])
    cache.set('trades', tradesList,timeout=10800)

@app.before_request
def initlializeSampleData():
    storeStockData()
    storeSampleTradesData()

@app.route('/stockService/calculatePerTrade', methods=['POST'])
def calculatePerTrade():
    """
    Sample input json
    {"trade" : {"symbol":"ALE","quantity":150,"indicator":"Buy","tradePrice":6598}},
     "marketPrice":200
    }
    """
    try:
        reqJson = request.get_json()
        reqTrade = reqJson.get('trade')
        marketPrice = reqJson.get('marketPrice')
        
        stocks = cache.get('stocks')
        stkObject = stocks.get(reqTrade.get('symbol'))
        
        divYield = stkObject.getDividendYield(marketPrice)
        pe = stkObject.getPERatio(marketPrice)
        
        #record trade data
        newTrade= [reqTrade.get('symbol'),int(time.time()),reqTrade.get('quantity'),reqTrade.get('indicator'),reqTrade.get('tradePrice')]
        trades = cache.get('trades')
        trades.append(newTrade)
        cache.set('trades',trades,timeout=10800)
        
        stkPrice = stkObject.getVolWeightedPrice(trades)
        
        result = {'divYield':divYield,'peRatio':pe,'stkPrice':stkPrice}
    except Exception as e:
        print(str(e))
        return jsonify('Exception in calculatePerTrade: '+str(e))
    
    return jsonify(result)        


@app.route('/stockService/calculateAllShareIndex', methods=['GET'])
def calculateAllShareIndex():
    try:
        stocks = cache.get('stocks')
        trades = cache.get('trades')
        allSharePrice = 1
        numTx = 1
        for stock in stocks.values():
            #for each stock type
            price = 1
            tradeCount = 0
            price, tradeCount = stock.getMeanParams(trades)
            allSharePrice *= price
            numTx += tradeCount
        
        result = {'AllShareIndex': allSharePrice**(1/numTx)}
            
    except Exception as e:
        print(str(e))
        return jsonify('Exception in calculateAllShareIndex: '+str(e))
    
    return jsonify(result) 

if __name__=='__main__':
    app.run('0.0.0.0')