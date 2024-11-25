
from firebase_admin import firestore, initialize_app, credentials
import os

cred = credentials.Certificate(os.path.join(os.path.dirname(__file__), "../skill_starter.json"))

initialize_app(cred)
db = firestore.client()

user_collection = db.collection('users')
learning_collection = db.collection('learnings')