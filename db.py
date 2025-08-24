import json 

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
            # Simple password storage (not secure for production, but good for learning)
            users[email] = {'name': name, 'password': password}
        
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
            stored_password = users[email]['password']
            if stored_password == password:  # Simple password comparison
                return users[email]['name']  # Login successful, return user's name
        
        return None # Incorrect email or password
