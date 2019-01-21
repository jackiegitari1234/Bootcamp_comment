
from register import User
from models import Comment

def main():
    print("Welcome to Commentor\n")


    while True:
        option = main_choice("Pick a choice to proceed: \n 1. Sign up \n 2. Quit")

        if option != 1 and option != 2:
            print('Invalid choice')

        else:
            firstname = enter_detail('Firstname')
            lastname = enter_detail('lastname')
            username = enter_detail('username')
            password = enter_detail('password')
            
            user = User(firstname, lastname, username, password)
            user.save()

            while True:
                action = main_choice('Pick an action:\n 1. Post comment 2. View comments')

                if option != 1 and option != 2:
                    print('Invalid choice')

                else:                
                    post_comment()
                    break


def main_choice(message):
    print(message)

    option = int(input())
    return option

def enter_detail(value):
    field = input('Enter {}: '.format(value))
    return field    

def post_comment():
    comment = Comment()

    while True:
        new_comment = input('\nEnter comment: ')

        if not new_comment:
            print('Comment cannot be empty!\n')

        else:

            data = {
                'body': new_comment,
                'author': 1
            }
            comment.save(data)

            print('Comment posted successfully!')
            break

    

if  __name__ == "__main__":
    main()