import firebase_admin
from firebase_admin import credentials, db


# Initialize Firebase Admin SDK
def initialize_firebase():
    # Replace with your Firebase service account key file
    cred = credentials.Certificate("../Credentials.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://code-vipassana-fd690-default-rtdb.asia-southeast1.firebasedatabase.app/"
        # your Firebase URL
    })


def create_user(userId, name, email):
    try:
        # Initialize Firebase (if not already done)
        initialize_firebase()

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

# Example usage
if __name__ == "__main__":
    user_id = "12345"
    name = "John Doe"
    email = "john.doe@example.com"

    create_user(user_id, name, email)
learning_path_id = "cybersecurity_6_month_path"  # Unique ID for this learning path

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

# Save the data to Firebase
save_learning_path(learning_path_id, learning_path_data)