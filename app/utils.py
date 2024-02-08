import pymongo
from .constants import db_user, db_pass


client = pymongo.MongoClient(
    f"mongodb+srv://{db_user}:{db_pass}@cluster0.ds5ggbq.mongodb.net/?retryWrites=true&w=majority"
)


def get_db():
    return client.get_database("starter_template")


db = get_db()