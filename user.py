import pyperclip
from user import User

class User:
  """
  This is a User class that creates new instances of other users
  """
  user_details= []
  
  def __init__(self, first_name, second_name, password):
        self.first_name= first_name
        self.second_name= second_name
        self.password= password
      
        
  #saving user details
  def save_user(self):
    """
    A save method that saves the details of the user
    """
    self.user_details.append(self)
    
  #deleting user's account
   
  def delete_account(self):
    """
    A delete method that tries to check whether the user's account is deletable
    """
    self.user_details.remove(self)
     
  #finding user by firstname
  @classmethod
  def find_by_first_name(cls,first_name):
     """  
      A method that finds the user using their first name
      Args:
      user: user to search for 
      returns:
      Name of the user searched for
     """
     for user in cls.user_details:
      if user.first_name == first_name:
       return user
         
    #displaying user
  @classmethod
  def display_user(cls):
  
     """
      A function that displays the user
     """
     return cls.user_details
    