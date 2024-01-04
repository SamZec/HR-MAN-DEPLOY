#!/usr/bin/env python3


# Assumed you have run 'pip install pymongo'
import pymongo
databaseName = 'hrman'
settings = {
  'host': 'iad2-c17-2.mongo.objectrocket.com:53259,iad2-c17-0.mongo.objectrocket.com:53259,iad2-c17-1.mongo.objectrocket.com:53259',
  'username': 'hrman',
  'password': 'hrman2024',
  'options': "?authSource={databaseName}&replicaSet=489d92853e0f433f8c793d062d606122".format(**locals())
}

host = "mongodb://{username}:{password}@{host}/{options}".format(**settings)
"""
try:
   conn = pymongo.MongoClient("mongodb://{username}:{password}@{host}/{options}".format(**settings))
   collectionNames = conn[databaseName].collection_names()
   print("Connected")
   print("Collection Names {}".format(collectionNames))
   conn.close()
except Exception as ex:
   print("Error: {}".format(ex))
   exit('Failed to connect, terminating.')

print("Finished") # Done!
"""
