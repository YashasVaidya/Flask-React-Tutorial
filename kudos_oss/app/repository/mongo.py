import os
from pymongo import MongoClient

COLLECTION_NAME = 'kudos' # Q: What is this?

class MongoRepository(object):
    def __init__(self):
        mongo_url = os.environ.get('MONGO_URL')
        self.db = MongoClient(mongo_url).kudos # Q: What is '.kudos"?

    def find_all(self, selector): # Q: What is selector?
        return self.db.kudos.find(selector) # Q: Why self.db.kudos?

    def find(self, selector):
        return self.db.kudos.find_one(selector)

    def create(self, kudo): # Q: What is kudo?
        return self.db.kudos.insert_one(kudo)

    def update(self, selector, kudo):
        return self.db.kudos.replace_one(selector, kudo).modified_count # Q: What is modified_count?

    def delete(self, selector):
        return self.db.kudos.delete_one(selector).deleted_count # Q: What is deleted_count?

# Q: What does exporting environment variable mean?
# Q: What is an environment variable?
