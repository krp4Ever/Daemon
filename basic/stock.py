#!/usr/bin/python
import tushare as ts
from db.mongo import connect_mongo
import json

def loadStockBasics():
	df = ts.get_stock_basics()
	db = connect_mongo('127.0.0.1',27017,"","","stock_db")
	db.stockBasics.insert(json.loads(df.to_json(orient="records")))


