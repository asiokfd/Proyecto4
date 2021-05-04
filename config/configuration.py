import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

dburl = os.getenv("URL")
#password= os.getenv ("pass")
print(dburl)
if not dburl:
    raise ValueError("no tienes url mongodb")


client = MongoClient(dburl)
db = client.get_database()
collection = db["politicos"]

#client = pymongo.MongoClient("mongodb+srv://asiokfd:<" + pass + ">@cluster0.zlghr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#db = client.test