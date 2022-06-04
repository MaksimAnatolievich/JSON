from services import update_user, get_users
username = input("Введите имя пользователя\n")
new_password = input("Введите новый пароль\n")

update_user(username, new_password)
print(get_users())