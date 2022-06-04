def validate_username(username):
    if len(username) > 20 or len(username) < 4:
        raise Exception('username length is in correct')