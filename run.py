#!/usr/bin/env python3.6
from credentials import Credentials
import pyperclip
from user import User

def create_user(first_name, second_name, password):
  """
  function that creates user
  """
  new_user=(first_name, second_name, password)
  return new_user

def create_credentials(first_name, second_name, password):
  """
  function that creates credentials
  """
  new_credentials=(first_name, second_name, password)
  return new_credentials
 
def display_info(account_name):
   """
   function that displays user's info
   """
   return Credentials.display_info(account_name)

def delete_info(info):
  """
  function that deletes info
  """
  return Credentials.delete_info()

def copy_credentials(first_name):
  """
  function that copies credentials
  """
  return Credentials.copy_credentials(first_name)

def save_user(user):
  """
  function that saves user
  """
  return User.save_user(user)

def save_credentials(credentials):
  """
  function that saves credentials
  """
  return Credentials.save_credentials(credentials)

def main():
    first_name= input("What is Your Name?")
    print(f"Hello {first_name},welcome to Password Locker:")
    print('\n')
    while True:
        print ('\n')
        print (r"*"*30)
        print ('\n')
        print("="*60)
        print("Use these short codes to navigate through Password_Locker:\n ln to log in \n ca to create a new account. \n ex to exit")
        print("="*60)
        print('\n')
        short_code = input().lower()
        if short_code == 'ca':
            print("Enter First Name ...")
            first_name = input()
            print("Enter Last Name ...")
            last_name = input()
            print("Do you want to input your own password or have one generated for you? Use short codes\n'gp\' to generate password.\n \'cyo\' to choose your own password \n \'ex\' to exit... ")
            password_choice = input()
            password = ''
            if password_choice == 'cyo':
                password = password.join(
                    input("Enter a password of your choice..."))
            elif password_choice == 'gp':
                print("Enter the length of the password you wish to generate eg 9 ")
            elif password_choice == 'ex':
                print('See you.........')
                break
            else:
                print("Sorry I didn\'t get that. Please try again")
            # Create and save new user
            save_user(create_user(first_name, last_name, phone_number,email,user_name, password))
            print('\n')
            print(f"New Account for {first_name} {last_name} created.")
            print('\n')
            print(
                f"Your password is {password} :-Use it to log in using short code ln")
            print('\n')
        elif short_code == 'ln':
            print('\n')
            print("Enter your account details to log in: \n Enter your username...")
            username = input()
            print("Enter your password...")
            password = input()
            account_exist = check_user(user_name, password)
            if account_exist == user_name:
                print('\n')
                print(
                    f"Welcome to your Password locker account {first_name}: \n Please choose an option to continue...")
                print('\n')
                while True:
                    print('\n')
                    print("Navigation short codes: \n cc to create new credentials: \n dc to display credentials: \n sc to search credentials: \n rm to remove or delete credentials: \n copy to copy credentials: \n ex to exit")
                    print('\n')
                    short_code = input().lower()
                    if short_code == 'cc':
                        print('\n')
                        print("Enter your credential details")
                        print("Enter account type... eg \'google\'")
                        
                        while True:
                            print("Do you want to input your own password or have one generated for you? Use short codes\n'gp\' to generate password.\n \'cyo\' to choose your own password \n \'ex\' to exit... ")
                            password_choice = input()
                            if password_choice == 'cyo':
                                password = input(
                                    "Enter a password of your choice...")
                                break
                            elif password_choice == 'gp':
                                print(
                                    "Enter the length of the password you wish to generate eg 9 ")
                                pass_len = int(input())
                                password = rand_pass(pass_len)
                                break
                            elif password_choice == 'ex':
                                print('See you.....')
                                break
                            else:
                                print("Sorry I didn\'t get that. Please try again")
                        save_credentials(create_credentials(first_name,second_name,password))
                        print(' \n')
                        print(
                            f'Credential Created:\n Account type: {site_name}  \n Account Username: {user_name} \n Account Password: {password}')
                        print('\n ')
                    elif short_code == 'dc':
                        if display_credentials(user_name):
                            print("Here is a list of your credentials:")
                            print('\n')
                            for credential in display_credentials(user_name):
                                print(f"Credential Created:\n Account type: {site_name} \n Account Username: {user_name} \n Account Password: {password}")
                        else:
                            print("You don\'t have any credentials yet")
                    elif short_code == "sc":
                        print("Enter the Account Name you want to search for")
                        site_name = input().lower()
                        if find_by_site_name(site_name):
                            search_credential = find_by_site_name(site_name)
                            print(f"Account Name : {search_credential.site_name}")
                            print('-' * 50)
                            print(f"User Name: {search_credential.username} Password :{search_credential.password}")
                            print('-' * 50)
                        else:
                            print("That Credential does not exist")
                            print('\n')
                    elif short_code == 'rm':
                        print("Enter the account type of the credential you wish to delete:...")
                        site_name = input()
                        if find_by_site_name(site_name):
                            credential_to_delete = find_by_site_name(site_name)
                            print("_"*50)
                            credential_to_delete.delete_credentials()
                            print('\n')
                            print("Credential successfully deleted!")
                        else:
                            print(" We couldin\'t find the credentials associated with the account name you typed.")
                    elif short_code == "copy":
                        print(' \n')
                        site_name = input(
                            'Enter the site name for the credential password to copy: ')
                        if find_by_site_name(site_name):
                            credential_to_copy = find_by_site_name(site_name)
                            print("_"*50)
                            credential_to_copy.copy_credentials(site_name)
                            print('\n')
                            print("Credential successfully copied")
                    elif short_code == "ex":
                         print('Goodbye.....')
                         break
                    else:
                        print("I didn\'t get that, please try again")
            else:
                print(
                    f"Sorry, we couldn\'t' find any account under the name {user_name}")
                print('\n')
        elif short_code == 'ex':
            print('See you...')
            break
        else:
            print("I really did not get that, please use the short code ")
print('\n')
if __name__ == '__main__':
    main()
