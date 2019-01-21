users = []

class User():


    def save(self, data):
        users.append(data)

    @staticmethod 
    def login(username, password):
        
        for user in users: 
            # user exists
            if user["username"] == username:
                
                if user["password"] == password:
                    print("Signed in as {}".format(user["username"]))
                else:
                    print("Password for {} is incorrect".format(user["username"]))
            else:
                print("User does not exist")


            
     
        
    


