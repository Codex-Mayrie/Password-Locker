#!/usr/bin/env python3.6
from credentials import Credentials
import pyperclip
from user import User

def create_user(first_name, second_name, password):
  """
  function that creates user
  """
  new_user=User(first_name, second_name, password)
  return new_user

def create_credentials(account_name,first_name,info_password):
  """
  function that creates credentials
  """
  new_credentials=Credentials(account_name,first_name,info_password)
  return new_credentials
 
def display_info():
   """
   function that displays user's info
   """
   return Credentials.display_info()

def delete_info(credentials):
  """
  function that deletes info
  """
  credentials.delete_info()

def copy_credentials(first_name):
  """
  function that copies credentials
  """
  return Credentials.copy_credentials(first_name)

def save_users(user):
  """
  function that saves user
  """
  user.save_user()
  
def check_user(first_name):
    '''
    '''
    return User.find_by_first_name(first_name) 
def find_by_user_name(first_name):
    '''
    '''
    return Credentials.find_by_user_name(first_name) 

def gen_password():
    """
    Function that generates password
    """
    gen_password= Credentials.gen_password()
    return gen_password

def save_credentials(credentials):
  """
  function that saves credentials
  """
  credentials.save_credential()



def main():
    
    first_name= input("What is Your Name?")
    print(f"Hello {first_name}")
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
            password_choice=input().lower()
            if password_choice == 'cyo':        
                password=input("Enter a password of your choice...").strip()    
            elif password_choice=='gp':
                print("Enter the length of the password you wish to generate eg 6 ")
                password=gen_password()
            
            elif password_choice == 'ex':
                print('See you.........')
                break
            else:
                print("Sorry I didn\'t get that. Please try again")
            save_users(create_user(first_name, last_name, password))
            print('\n')
            print(f"New Account for {first_name} {last_name} created.")
            print('\n')
            print(
                f"Your password is {password} :-Use it to log in using short code ln")
            print('\n')
        elif short_code == 'ln':
            print('\n')
            print("Enter your account details to log in: \n Enter your first Name...")
            user_name = input()
            print("Enter your password...")
            pass_word = input()
            account_exist = check_user(user_name)
            if account_exist.first_name == user_name and account_exist.password == pass_word:
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
                        print("Enter Account name")
                        acc=input()
                        print("Enter Username")
                        usName=input()
                        print("Enter password")
                        pasWd=input()
                            
                        save_credentials(create_credentials(acc,usName,pasWd))
                        print(' \n')
                        print(f"Credential Created: Account type: {acc}  Account Username: {usName}  Account Password: {pasWd}")
                        print('\n ')
                    elif short_code == 'dc':
                        if display_info():
                            print("Here is a list of your credentials:")
                            print('\n')
                            for credential in display_info():
                                print(f"Credential Created:\n Account type: {credential.account_name} \n Account Username: {credential.first_name} \n Account Password: {credential.info_password}")
                        else:
                            print("You don\'t have any credentials yet")
                    elif short_code == "sc":
                        print("Enter the Account Name you want to search for")
                        first_name = input().lower()
                        if find_by_first_name(first_name):
                            search_credential = find_by_first_name(first_name)
                            print(f"Account Name : {search_credential.first_name}")
                            print('-' * 50)
                            print(f"User Name: {search_credential.username} Password :{search_credential.password}")
                            print('-' * 50)
                        else:
                            print("That Credential does not exist")
                            print('\n')
                    elif short_code == 'rm':
                        print("Enter the user name of the credential you wish to delete:...")
                        us_name = input()
                        found=find_by_user_name(us_name)
                        if found.first_name == us_name:
                            found.delete_info()
                            
                            print("_"*50)
                            print(f"Deleted {found.first_name}")
                            
                        else:
                            print(" We couldn't find the credentials associated with the user name you typed.")
                    elif short_code == "copy":
                        print(' \n')
                        first_name = input(
                            'Enter the first name for the credential password to copy: ')
                        if find_by_first_name(first_name):
                            credential_to_copy = find_by_first_name(first_name)
                            print("_"*50)
                            credential_to_copy.copy_credentials(first_name)
                            print('\n')
                            print("Credential successfully copied")
                    elif short_code == "ex":
                         print('See you.....')
                         break
                    else:
                        print("I didn\'t get that, please try again")
            else:
                print(
                    f"Sorry, we couldn\'t' find any account under the name {first_name}")
                print('\n')
        elif short_code == 'ex':
            print('See you...')
            break
        else:
            print("I really did not get that, please use the short code ")
print('\n')
if __name__ == '__main__':
    main()
