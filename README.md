# Super Simple Stocks

This is a service based module which fulfills the below requirements

Requirements<br>
Provide working source code that will :<br>
a. For a given stock,<br>
  i. Given a market price as input, calculate the dividend yield<br>
  ii. Given a market price as input, calculate the P/E Ratio<br>
  iii. Record a trade, with timestamp, quantity of shares, buy or sell indicator and
  trade price<br>
  iv. Calculate Volume Weighted Stock Price based on trades in past 15 minutes <br>
b. Calculate the GBCE All Share Index using the geometric mean of prices for all stocks

Constraints & Notes:<br>
Written in one of these languages:Python

Required libs:<br>
flask<br>
flask_caching - for caching the stocks and trades data in memory

Two Endpoints:<br>
URL: http://localhost:5000/stockService/calculatePerTrade<br>
Method: POST<br>
Request JSON - {"trade" : {"symbol":"ALE","quantity":150,"indicator":"Buy","tradePrice":6598},"marketPrice":200}<br>
Calculates data points mentioned in point a<br>
<br>
URL: http://localhost:5000/stockService/calculateAllShareIndex<br>
Method: GET<br>
No input params<br>

Setup:<br>
Run   stockservice.py file locally and call the webservices
