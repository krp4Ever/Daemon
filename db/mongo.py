#!/usr/bin/python
from pymongo import MongoClient

def connect_mongo(host,port,username,password,db):
	"""a util for making a connection to mongo"""
	if username and password:
		mongo_uri = "mongodb://%s:%s@%s:%s/%s" %(username,password,host,port,db)
		conn = MongoClient(mongo_uri)
	else:
		conn = MongoClient(host,port)
	return conn[db]

def read_mongo(db,collection,query={},host="localhost",port="2701",username=None,password=None,no_id=True):
	"""Read from mongo and store into Dataframe """
	db = connect_mongo(host=host,port=port,username=username,password=password,db=db)
	cursor = db[collection].find(query)
	df = pd.DataFrame(list(cursor))
	
	if no_id:
		del df['_id']
	return df
