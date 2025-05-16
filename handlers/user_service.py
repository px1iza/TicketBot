import json
from datetime import datetime
import os

USERS_FILE = 'data/users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as f:
            json.dump([], f)

    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def add_user(user_data):
    users = load_users()
    if any(user["id"] == user_data["id"] for user in users):
        return False

    users.append(user_data)
    save_users(users)
    return True