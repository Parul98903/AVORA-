from datetime import datetime

def create_user(name, email, password):
    return {
        "name": name,
        "email": email,
        "password": password,
        "created_at": datetime.utcnow()
    }