from crud import module as ml
import pymongo
# MongoDB
myclient = pymongo.MongoClient("mongodb+srv://prataplyf:Ashish12@ashish-hbjy0.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient.crud
article = mydb["article"] # academy funnel

# secret key for JWT Token used at user_login page
master_key= "wharfstreetstrategies_masterKey_for_spaceIZ_Bounty"
