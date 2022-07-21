# Получать всех юзеров  из JSON

import json
from os import path
from exceptions import UserAlreadyExistsException
from exceptions import UserNotFoundException
filename = "D:\Программирование\python\JSON\Data.json"
listObj = []


def get_users():
    if path.isfile(filename) is False:
        raise Exception("File not found")
    with open(filename) as fp:
        return (json.load(fp))


# Добавить юзера из JSON
def create_user(username, password, age):
    users = get_users()
    # Verify existing list
    users.append({"username": username,
                  "password": password,
                  "age": age})

    save_users(users)


def delete_user(username):
    users = get_users()
    for i in users:
        if i.get('username') == username:
            users.remove(i)
    save_users(users)


def save_users(users):
    with open(filename, 'w') as json_file:
        json.dump(users, json_file,
                  indent=4,
                  separators=(',', ': '))


# обновить пароль юзера по username
def update_user(username, new_password):
    users = get_users()
    try:
        user = get_user(username)
        if not user:
            raise UserNotFoundException(username)
        for i in users:
            if i.get('username') == username:
                i.update({"password": new_password})
        save_users(users)
    except UserNotFoundException as e:
        print(str(e))


# hard level


# def delete_user(username):
#     users = get_users()
#     try:
#         success = False
#         for i in users:
#             if i.get('username') == username:
#                 users.remove(i)
#                 success=True
#         if not success:
#             raise Exception("UserDoesNotExists")
#     except Exception as e:
#         print(str(e))
#     save_users(users)


def delete_user(username):
    users = get_users()
    try:
        user=get_user(username)
        if not user:
            raise UserNotFoundException(username)

        users.remove(user)


    except UserNotFoundException as e:
        print(str(e))
    save_users(users)

def get_user(username):
    users = get_users()
    for user in users:
        if user.get('username') == username:
            return user

def create_user(username, password, age):
    users = get_users()
    try:
        user = get_user(username)
        if user:
            raise UserAlreadyExistsException(username)
        users.append({"username": username,
                  "password": password,
                  "age": age})

        save_users(users)
    except UserAlreadyExistsException as e:
        print(str(e))



