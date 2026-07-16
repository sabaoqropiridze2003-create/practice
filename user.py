class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.active = True

    def deactivate(self):
        self.active = False

    def change_email(self, new_email):
        if "@" not in new_email:
            raise ValueError("Invalid email address")
        else:
            self.email = new_email

    def greet(self):
        return f"Hello, {self.name}!"
