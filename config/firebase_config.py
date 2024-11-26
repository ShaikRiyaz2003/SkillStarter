
from firebase_admin import firestore, initialize_app, credentials
import os



cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "skillstarter-e0d14",
  "private_key_id": "b026ca72744ed37ee39d83f2c8c58360136028ac",
  "private_key": ="-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCvHxgr3N6THf2C\n0QtcM0KrMvIw+KD44MCiPXUodfuvhX1dnSUWWJohdbuzES0XX5BuG1/TV34Htcjx\nmtZnRVAiDFYmHWjXO7Q0Lzmj2kkiDAmDmzIxxGDctI9TwvIvdwDS+1YbEq7Es9Zo\nStAfFYzLTCQbajCx4CF7KTQMAex298uqdIbgCbaNKUk8tniO9YADePHwWGGWYEZg\nlQA8QzuROgPVvfj+AT77DMxTKIanxNb33FT7ShQwQ7QNdGCOIHU2yzmBW8ehXGEl\nLiI3w3/Aidz15D+WGEr/KgeUNFBbYpaIy4++eEH2u5jtN+HaDneepJO0IBH/judg\n/TxHpjK1AgMBAAECggEAAJ8uJH26YDBZ+Mk9CDATm2ycL1aHdjEqGryRujnAOCCg\ngzp7HSF/m2doUE70mrtXbz5APVpd4ErupZ9eOOvZYhcqhfEfZBNz5NmKeicpkLbi\nBvcZzjmhx5086XG529EWDim5TD62CYz2UaF7LExIMMw0HQRoAg56X/StMoiEalNR\nmLlPwioXz+VZ+IvNpa8E4J+rOkASCpVdELWcVCbETzAIW6p0xngtmSjE7dTelyz/\nZwDXdMrw3euRSRsSUgniPR8cIE8ral6+SJ6h5bIL3G10PNDB7g/5R/uwKmlcPSoT\nOX3mJ7ZvAV44AYgYJPM7vDzBaSSRzIFPq9YuI54HMwKBgQD1q8cSp8pKzDqgOUL2\nE7TO1yoKeeuRTulm2hMD2ALlrMc9GOzruzHK6llSl3r9X+Fg20yCBsrzN4fq6Pal\nY+vzrH5o9ZJCWbosXpnA/nKYsd8v9zDzCyQ/8hUZ63h9uP6ehsTXdb7vNhYrsIiK\nZYnqIlIZUR3b9IAAA4nSjw+5WwKBgQC2e/kpjCGF8usQ+nVjJGEwTQqHns1N2sQo\nmo58RK64u+rcMRWnlLYTbsw9xnX0moVspj/jo6Pq41prADvqIRHET/CSQfkhA7Dj\nhFWLN9aBi0txZscpURUb7jOtocY37dgLaBecN8tYeKvWBh5C1Xa1AzVFlRYT22lc\nQY+aWXZxLwKBgQCReZ7wlRtdH4K3zjCwtwqiURc8DOZJrYjYttn7tLZCewWgUFo7\nXSYnGo66MalK0LQNPs8XUB5t17xMhpdHaNwX91UDoidx0uBD1eEGP6ZsdSfMp3v8\n7+QPWbLVHnLDQADGrtdxHvBphoWqaWbxTR9V3ezvwPEFhsslNvMuFDkjcQKBgEtY\nJokb/Z9jq+CnuJ4FoEckGAvk6lmR0Nn+7oOqjAVkOVVOwuUdRowBfDypW3xx7FLu\n1YQ0xXIvCt8RCqvhmYdXhjmtGaKi9n8J3ZQMqvlzvOOGjwalHrUYhafUGpZvEnur\nL8xlUQUnVbOZdRcdMdUNDQq8wo/SUM8xlowhEgErAoGBAL95q0OaLnwt6XM3SgFD\npj7SoIY/v7cvP+fWLr2dqnEEPA94eEK+uHf6J9QKXCnYughgYq5eKrjy+pxl5sSY\no0rN2q9VlYv3WM5FR/RBfRs6aVgXQ5Jyn8eg2UP/K5NS6Xrgo3VRiQK0zD5EELql\n0/H7V+IaD/KQdjQyZUYZUpRS\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-krgrp@skillstarter-e0d14.iam.gserviceaccount.com",
  "client_id": "110476956782590184428",
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
