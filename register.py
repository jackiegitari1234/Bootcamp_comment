users = []

class User():

    def __init__(self, firstname,lastname,username,password):
        self.firstname = "firstname"
        self.lastname = "lastname"
        self.username = "username"
        self.password = "password"
        self.lastLoggedIn = None
        self.role = 3
        self.loggedIn = False

    def save(self):
        users.append(self)
    


    