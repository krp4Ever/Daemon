#!/usr/bin/python
import tushare as ts
from .db.mongo import connect_mongo
import json

def getStockBasics():
	df = ts.get_stock_basics()
	connect = Connection('127.0.0.1',port=27017)
	connect.db.stockBasics.insert(json.loads(df.to_json(orient="records")))


