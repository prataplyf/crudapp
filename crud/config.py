from crud import module as ml
import pymongo
# MongoDB
myclient = pymongo.MongoClient("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
mydb = myclient.db_name
article = mydb.schema_name # academy funnel

# secret key for JWT Token used at user_login page
master_key= "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
