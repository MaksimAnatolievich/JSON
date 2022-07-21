class UserAlreadyExistsException(Exception):
    def __init__(self, user, message="такой юзер уже существует"):
        self.user = user
        self.message = message
        super().__init__(f"{self.message}, {self.user}")
class UserNotFoundException(Exception):
    def __init__(self, user, message="такого лузера не существует"):
        self.user = user
        self.message = message
        super().__init__(f"{self.message}, {self.user}")