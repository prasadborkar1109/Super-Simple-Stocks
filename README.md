# python
Python project repository

Super Simple Stocks - This is a service based module which fultills the below requirements

Requirements
Provide working source code that will :-
a. For a given stock,
  i. Given a market price as input, calculate the dividend yield
  ii. Given a market price as input, calculate the P/E Ratio
  iii. Record a trade, with timestamp, quantity of shares, buy or sell indicator and
  trade price
  iv. Calculate Volume Weighted Stock Price based on trades in past 15 minutes
b. Calculate the GBCE All Share Index using the geometric mean of prices for all stocks

Constraints & Notes
Written in one of these languages:Python

Required libs:
flask
flask_caching - for caching the stocks and trades data in memory

Two Endpoints:
URL: http://localhost:5000/stockService/calculatePerTrade
Method: POST
Request JSON - {"trade" : {"symbol":"ALE","quantity":150,"indicator":"Buy","tradePrice":6598},"marketPrice":200}
Calculates data points mentioned in point a

URL: http://localhost:5000/stockService/calculateAllShareIndex
Method: GET
No input params

Setup:
Run   stockservice.py file locally and call the webservices
