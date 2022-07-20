from JSON.validation import validate_username,validate_age,validate_password
from services import create_user, get_users

while True:
    try :
        username = input("Введите имя пользователя\n")
        password = input("Введите пароль\n")
        age = int(input("Введите возраст\n"))
        validate_username(username)
        validate_password(password)
        validate_age(age)
    except Exception as error:
        print(f'Данные некорректные: {error}')
    else:
        break
create_user(username, password, age)
print(get_users())
