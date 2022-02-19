#!/usr/bin/env python3.8

import email
from hashlib import new
from unicodedata import name

from click import password_option
from user import user
from credential import credential


def create_user(user_name,password):
    '''
    Function to create a new user
    '''
    new_user = user(user_name,password)
    return new_user

 
def save_users(user):
    '''
    Function to save user
    '''  
    user.save_user() 

def del_credential(credential):
    '''
    Function to delete a credential account
    '''  
    credential.delete_credential  



def main():
    print("Welcome to life made simple with password locker. What is your user name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("use this short codes : nu - create a new user, aa - create password for an app, dl - delete account. sa - save account, vac - view account credentials")

        short_code = input().lower()

        if short_code == 'nu':
            print("user") 

            print("user name....")
            user_name = input()

            print ("password")
            password = input()

            print ("email address")
            email = input()

            save_users(create_user(name,password,email))# creating and saving a user
            print ('\n')
            print (f"new user { user_name} {password} created")
            print ('\n')    


       

 