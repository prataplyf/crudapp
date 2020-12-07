from crud import module as ml
import pymongo
# MongoDB
myclient = pymongo.MongoClient("mongodb+srv://prataplyf:ashish12@ashish-hbjy0.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient.crudapp
article = mydb.posts # academy funnel

# secret key for JWT Token used at user_login page
master_key= "demo_test_crudapp"
