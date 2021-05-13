import os

from pymongo import MongoClient

client = MongoClient('mongodb://' + os.environ['MONGODB_USERNAME'] + ':' +
                     os.environ['MONGODB_PASSWORD'] + '@' +
                     os.environ['MONGODB_HOSTNAME'] + ':27017/' +
                     os.environ['MONGODB_DATABASE'])
db = client[os.environ.get("MONGODB_DATABASE", 'taskrunner')]
