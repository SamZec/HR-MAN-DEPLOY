#!/usr/bin/env python3


databaseName = '/hrman?replicaSet=489d92853e0f433f8c793d062d606122'
user = 'hrmani:'
password = 'hrman2024@'
host_1 = 'iad2-c17-2.mongo.objectrocket.com:53259,'
host_2 = 'iad2-c17-0.mongo.objectrocket.com:53259,'
host_3 = 'iad2-c17-1.mongo.objectrocket.com:53259'
host = user + password +  host_1 + host_2 + host_3 + databaseName
