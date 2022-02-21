#!/usr/bin/env python3.8

import email
from hashlib import new
from unicodedata import name

from click import password_option
from user import user
from credential import credential


# user function for behaviours expected
def create_user(user_name, password, email):
    '''
    Function to create a new user
    '''
    new_user = user(user_name, password, email)
    user.save_user
    return new_user


def login_user(user_name, password):
    '''
    Function to create log in
    '''
    login_user = user(user_name, password)
    user.login_user
    return login_user


# def save_user(user):
#     '''
#     Function to save user
#     '''
#     user.save_user()

def save_credential(credential):
    '''
    Function to save credential in user
    '''
    credential.save_credential(credential)
    return credential


def create_credential(user_name, password, email):
    '''
    Function to create a new credential in a user
    '''
    new_credential = credential(user_name, password, email)
    return new_credential


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()


# credential functions for behaviours expected

def create_credential(user_name, password, email):
    '''
    Function to create a new credential
    '''
    new_credential = credential(user_name, email, password)
    credential.save_credential
    return new_credential

# def save_credentials(credentials):
#     '''
#     Function to save credential
#     '''
#     credential.save_credential()


def del_credential(credential):
    '''
    Function to delete a credential account
    '''
    credential.delete_credential()


def password_option_credential(credential):
    '''
    Function input password without restriction
    '''
    credential.password_option_credintial


# calling funcion
def main():
    print("Welcome to life made simple with password locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("use this short codes : nu - create a new user, li-log in, suc - save credential in user, cc - create credential in user, dl - delete account, ex -exit account")

        short_code = input().lower()

        if short_code == 'nu':
            print(" create user")

            print("user name....")
            user_name = input()

            print("password")
            password = input()

            print("email address")
            email = input()

            # creating and saving a user
            user.save_user(create_user(user_name, password, email))
            print('\n')
            print(f"new user { user_name} {password} {email} created")
            print('\n')

        elif short_code == 'li':
            print("Log in to your account")

            print("user_name")
            user_name = input()

            print("password")
            password = input()

        elif short_code == 'suc':
            print("save other app credential")

            print("user name..")
            user_name = input()

            print("password")
            password = input()

            
            # creating and saving a user's credential
            credential.save_credential(save_credential(credential))
            print('\n')
            print(f"new application { user_name} {password} saved")
            print('\n')

        elif short_code == 'cc':
            print("create app in password locker")

            print("user name..")
            user_name = input()

            print("password")
            password = input()

            print("email address")
            email = input()

            # creating and saving a user's credential
            credential.save_credential(create_credential(name, password, email))
            print('\n')
            print(f"new application { user_name} {password} {email} created")
            print('\n')

        elif short_code == 'dl':
            print("app deleted")

        elif short_code == 'ex':
            print("Thank you for using our app..")

        else:
            print("Please use the short codes")


if __name__ == '__main__':

    main()
