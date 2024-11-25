import firebase_admin
from firebase_admin import credentials, db
import os
from fastapi import APIRouter, HTTPException
credentials_dict = {
    "type": "service_account",
    "project_id": "code-vipassana-fd690",
    "private_key_id": "0a6ef67d7fafd46689421f1fcf564e6b81a7eff3",
    "private_key": os.environ.get("FIREBASE_PRIVATE_KEY").replace('\\n', '\n'),
    "client_email": os.environ.get('FIREBASE_CLIENT_EMAIL'),
    "client_id": os.environ.get('FIREBASE_CLIENT_ID'),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-72wvc%40code-vipassana-fd690.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}
cred = credentials.Certificate(credentials_dict)
firebase_admin.initialize_app(cred, {
    "databaseURL": os.environ.get("FIREBASE_DATABASE_URL")
    # your Firebase URL
})


def create_user(userId, name, email):
    try:
        # Firebase reference for the 'users' node
        user_ref = db.reference(f"/users/{userId}")  # Use the userId as the key

        # Create user data dictionary
        user_data = {
            "userId": userId,
            "name": name,
            "email": email
        }

        # Set the user data in Firebase under the /users/{userId} path
        user_ref.set(user_data)  # This will create a new user or overwrite existing user

        print(f"User {name} successfully created in Firebase!")
    except Exception as e:
        print(f"Error creating user: {e}")

# Function to push learning path data to Firebase
def save_learning_path(learning_path_id, learning_path_data):
    try:
        # Initialize Firebase (if not already done)
        #initialize_firebase()

        # Firebase reference for the 'learning_paths' node
        learning_path_ref = db.reference(f"/learning_paths/{learning_path_id}")  # Use the learning_path_id as the key

        # Set the learning path data in Firebase
        learning_path_ref.set(learning_path_data)

        print(f"Learning path {learning_path_data['learning_path_name']} successfully saved to Firebase!")
    except Exception as e:
        print(f"Error saving learning path: {e}")

# Example JSON data (learning path data)
learning_path_data = {
    "learning_path_name": "6-Month Cybersecurity Professional",
    "learning_path_description": "A comprehensive 6-month plan to acquire professional-level cybersecurity skills with a focus on Machine Learning, Data Science, Networking, and DSA.",
    "due_date": "2025-05-25",
    "tasks": [
        {
            "task_name": "Cybersecurity Foundations",
            "task_deadline": "2024-12-25",
            "duration_period": "1 month",
            "task_description": "Build a strong foundation in core cybersecurity concepts.",
            "task_achievables": ["Understand fundamental security principles",
                                 "Learn about common threats and vulnerabilities"],
            "subtasks": [
                {
                    "subtask_name": "Network Security Basics",
                    "subtask_deadline": "2024-12-10",
                    "duration_period": "2 weeks",
                    "subtask_description": "Learn about network protocols, firewalls, and intrusion detection systems.",
                    "subtask_achievables": [
                        {
                            "reference_name": "Network Security Fundamentals",
                            "reference_link": "https://www.coursera.org/learn/network-security-fundamentals"
                        }
                    ]
                },
                {
                    "subtask_name": "Cryptography Essentials",
                    "subtask_deadline": "2024-12-25",
                    "duration_period": "2 weeks",
                    "subtask_description": "Understand encryption, decryption, and digital signatures.",
                    "subtask_achievables": [
                        {
                            "reference_name": "Cryptography I",
                            "reference_link": "https://www.coursera.org/learn/cryptography-i"
                        }
                    ]
                }
            ]
        },
        {
            "task_name": "Machine Learning for Cybersecurity",
            "task_deadline": "2025-02-25",
            "duration_period": "2 months",
            "task_description": "Apply machine learning techniques to cybersecurity challenges.",
            "task_achievables": ["Understand machine learning models",
                                 "Learn to apply ML algorithms in cybersecurity scenarios"],
            "subtasks": [
                {
                    "subtask_name": "Introduction to Machine Learning",
                    "subtask_deadline": "2025-01-10",
                    "duration_period": "1 month",
                    "subtask_description": "Learn the basics of machine learning algorithms and their applications.",
                    "subtask_achievables": [
                        {
                            "reference_name": "Machine Learning by Andrew Ng",
                            "reference_link": "https://www.coursera.org/learn/machine-learning"
                        }
                    ]
                }
            ]
        }
    ]
}

router = APIRouter()
@router.post("/create_user/")
async def api_create_user(userId: str, name: str, email: str):
    try:
        create_user(userId, name, email)
        return {"message": f"User {name} successfully created in Firebase!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating user: {e}")

@router.post("/save_learning_path/")
async def api_save_learning_path(learning_path_id: str, learning_path_data):
    try:
        save_learning_path(learning_path_id, learning_path_data.dict())
        return {"message": f"Learning path {learning_path_data.learning_path_name} successfully saved to Firebase!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving learning path: {e}")

# Include the router in your FastAPI app
# from fastapi import FastAPI
# app = FastAPI()
# app.include_router(router, prefix="/api")