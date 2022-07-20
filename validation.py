import re
def validate_username(username):
    if len(username) > 20 or len(username) < 4:
        raise Exception('username length is in correct')

def  validate_password(password):

    if len(password) < 7 or not re.search('\d+', password) :
        raise Exception('password is in correct')


def validate_age(age):
    if age < 0 or age > 120:
        raise Exception('age is in correct')
