import time
from utility import StockType


class Stock:
    

    def __init__(self, stkSymbol, stockType, lastDividend, fixedDividend, parValue):
        
        self.stkSymbol = stkSymbol
        self.stockType = stockType
        self.lastDividend = lastDividend
        self.fixedDividend = fixedDividend
        self.parValue = parValue
		
	
    def getDividendYield(self, marketPrice):
        if self.stockType == StockType.Common.name:
            return self.lastDividend / marketPrice
        elif self.stockType == StockType.Preferred.name:
            return (((self.fixedDividend / 100) * self.parValue) / marketPrice)
	
    def getPERatio(self, marketPrice):
        yieldedDividend = self.getDividendYield(marketPrice)
        return marketPrice/yieldedDividend if yieldedDividend!=0 else 0
	
    def getVolWeightedPrice(self, trades):
        price = 0
        quantity = 0
        currentTime = int(time.time())
        for trade in trades:
            if trade[0] == self.stkSymbol:
                if trade[1] > (currentTime - (15 * 60)):
                    price += trade[2] * trade[4]
                    quantity += trade[2]
                    
        return price/quantity
	
    def getMeanParams(self, trades):
        
        sumPrice = 1
        tradeCount = 0
        for trade in trades:
            sumPrice *= trade[4]
            tradeCount += 1
        return sumPrice, tradeCount
		