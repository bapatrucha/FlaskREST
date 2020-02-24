from models.user import UserModel

# users = [
#     UserModel(1,'Rucha', 'Rahul')
# ]
#
# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}

# def authenticate(username, password):
#     user = username_mapping.get(username, None) # get username from username_mapping,
#     print(user)                                            # if not found then None
#     if user and user.password == password: # to compare strings safely
#         return user

def authenticate(username, password):
    user = UserModel.findByUsername(username)
    print(user)
    if user and user.password == password:
        return user

# def identity(payload):
#     user_id = payload['identity']
#     print("user_id: ", user_id)
#     return userid_mapping.get(user_id, None)

def identity(payload):
    user_id = payload['identity']
    return UserModel.findByUserId(user_id)
