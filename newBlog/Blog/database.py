import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017/"
    DATABASE = None

    @staticmethod
    def initialize():
        try:
            client = pymongo.MongoClient(Database.URI)
            Database.DATABASE = client['fullstack']
        except Exception as e:
            print(f"Error during database initialization: {e}")

    @staticmethod
    def insert(collection, data):
        if Database.DATABASE is not None:
            Database.DATABASE[collection].insert_one(data)
            print("Document inserted successfully.")
        else:
            print("Error: Database connection not established.")

    @staticmethod
    def find(collection, query):
        if Database.DATABASE is not None:
            return Database.DATABASE[collection].find(query)
        else:
            raise ConnectionError("Error: Database connection not established.")

    @staticmethod
    def find_one(collection, query):
        if Database.DATABASE is not None:
            return Database.DATABASE[collection].find_one(query)
        else:
            raise ConnectionError("Error: Database connection not established.")
