from crud import module as ml
import pymongo
# MongoDB
myclient = pymongo.MongoClient("mongodb+srv://prataplyf:ashish12@ashish-hbjy0.mongodb.net/<dbname>?retryWrites=true&w=majority")
# mongodb+srv://ashishs:bHyoeB2R9CfRXUVb@wsstrategies.k0xsd.mongodb.net
mydb = myclient.crudapp
article = mydb.posts # academy funnel

# secret key for JWT Token used at user_login page
master_key= "demo_test_crudapp"
