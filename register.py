users = []

class User():


    def save(self, data):
        users.append(data)

    @staticmethod 
    def login(username, password):

        if len(users) == 0:
            return None

        user = [user for user in users if user['username'] == username][0]
        
        if user["password"] == password:
            print("Signed in as {}".format(user["username"]))
            return user
        else:
            print("Password for {} is incorrect".format(user["username"]))
            return None



            
     
        
    


