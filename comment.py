
from register import User

def main():
    print("Welcome to Commentor\n")

    user = User()


    while True:
        option = main_choice()

        if option != 1 and option != 2:
            print('Invalid choice')

        else:

            if option == 1:
                firstname = enter_detail('Firstname')
                lastname = enter_detail('lastname')
                username = enter_detail('username')
                password = enter_detail('password')

                data = {
                    'firstname': firstname,
                    'lastname': lastname,
                    'username': username,
                    'password': password
                }
                user.save(data)
            
            elif option == 2:
                username = enter_detail("username")
                password = enter_detail("password")
                user.login(username, password)

def main_choice():
    print("pick a choice to proceed: \n 1. Sign up \n 2. Sign in \n 3. Quit")

    option = int(input())
    return option

def enter_detail(value):
    field = input('Enter {}'.format(value))
    return field    

if  __name__ == "__main__":
    main()