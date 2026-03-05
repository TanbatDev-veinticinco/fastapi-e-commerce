from storage import db


def create_user(data):
    
    new_id = db.users_counter

    new_user = {
        "id": new_id,
        "email": data.email,
        "full_name": data.full_name
    }

    db.users[new_id] = new_user
    db.users_counter += 1

    return new_user

def get_all_user():
    return list(db.users.values())
