import json 
from werkzeug.security import generate_password_hash, check_password_hash

class Database:

    def insert(self, name, email, password):
        try:
            with open('user.json', 'r') as rf:
                users = json.load(rf)
        except (FileNotFoundError, json.JSONDecodeError):
            # If file doesn't exist or is empty/corrupt, start with an empty user dictionary
            users = {}

        if email in users:
            return False  # Email already exists
        else:
            # Hash the password for secure storage
            hashed_password = generate_password_hash(password)
            users[email] = {'name': name, 'password': hashed_password}
        
        with open('user.json', 'w') as wf:
            json.dump(users, wf, indent=4)
            return True  # Registration successful
        
    def search(self, email, password):
        try:
            with open('user.json', 'r') as rf:
                users = json.load(rf)
        except (FileNotFoundError, json.JSONDecodeError):
            return None # Cannot log in if user file is missing or corrupt

        if email in users:
            hashed_password = users[email]['password']
            if check_password_hash(hashed_password, password):  # Securely check password
                return users[email]['name']  # Login successful, return user's name
        
        return None # Incorrect email or password
