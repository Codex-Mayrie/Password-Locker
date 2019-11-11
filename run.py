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

    