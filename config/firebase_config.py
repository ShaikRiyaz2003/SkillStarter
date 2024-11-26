
from firebase_admin import firestore, initialize_app, credentials
import os



cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "skillstarter-e0d14",
  "private_key_id": os.environ.get("FIRESTORE_PRIVATE_KEY_ID"),
  "private_key": os.environ.get("FIRESTORE_PRIVATE_KEY"),
  "client_email": "firebase-adminsdk-krgrp@skillstarter-e0d14.iam.gserviceaccount.com",
  "client_id": os.environ.get("FIRESTORE_CLIENT_ID"),
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-krgrp%40skillstarter-e0d14.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
})

initialize_app(cred)
db = firestore.client()

user_collection = db.collection('users')
learning_collection = db.collection('learnings')