from function import register_user, all_show_user, one_show_user, one_show_age, update_user, delete_user


def main():
    print('=' * 4, 'Welcome to CRM Application', '=' * 4)
    print('[S]how: Show all users info')
    print('[A]dd: Add new user')
    print('[F]ind: Find one user info')
    print('[E]dit: Edit one user info')
    print('[Q]ite: Quit system')
    print('=' * 20)

    command = input('Your command > ')
    if command == 's' or command == 'S':
        all_show_user()


    elif command == 'a' or command == 'A':

        new_name = input('New user name > ')
        new_age = input('New user age > ')

        if new_age == '':
            print('age can\'t be blank')

        elif new_age.isdecimal() == False:
            print('Age is not positive integer')

        elif len(new_name) == 0:
            print('User name can\'t be blank')

        elif len(new_name) > 20:
            print('User name is too long(maximun is 20 characters)')


        elif int(new_age) < 0:
            print('Age is less than 0')

        elif int(new_age) > 120:
            print('Age is greater than 120')
        else:
            if register_user(new_name, int(new_age)):
                print(f'Add new user: {new_name}')



    elif command == 'f' or command == 'F':
        user_name = input('User name > ')
        one_show_user(user_name)


    elif command == 'q' or command == 'Q':
        print('Bye!')

    elif command == 'd' or command == 'D':
        delete_name = input('User name > ')
        delete_user(delete_name)
        print(f'User {delete_name} is deleted')


    elif command == 'e' or command == 'E':
        old_user_name = input('User name > ')
        print()
        new_user_name = input(f'New user name ({old_user_name})> ')
        age = one_show_age(old_user_name)
        new_user_age = int(input(f'New user age ({age}) > '))
        update_user(old_user_name, new_user_name, new_user_age)

    else:
        print(f'{command}: command not found')


if __name__ == '__main__':
    main()
