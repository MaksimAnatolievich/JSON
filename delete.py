from services import delete_user, get_users
username = input("Удалить имя пользователя\n")
delete_user(username)
print(get_users())