from services import create_user, get_users
username = input("Введите имя пользователя\n")
password = input("Введите пароль\n")
age = int(input("Введите возраст\n"))

create_user(username, password, age)
print(get_users())