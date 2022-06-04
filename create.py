from JSON.validation import validate_username
from services import create_user, get_users
while True:
    try :
        username = input("Введите имя пользователя\n")
        password = input("Введите пароль\n")
        age = int(input("Введите возраст\n"))
        validate_username(username)
    except Exception as error:
        print(f'Данные некорректные: {error}')
    else:
        break
create_user(username, password, age)
print(get_users())
