# Получать всех юзеров  из JSON

import json
from os import path

filename = "D:\Программирование\python\JSON\Data.json"
listObj = []


# Check if file exists

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

#обновить пароль юзера по username
def update_user(username, new_password):
    users = get_users()
    for i in users:
        if i.get('username') == username:
            i.update({"password": new_password})
    save_users(users)
