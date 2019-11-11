import pyperclip
import string

class Credentials: 
  """
  This is a class that creates new instances of user credentials
  """
    
  info_details=[]
    
  def __init__(self, account_name,first_name,info_password):
    
    self.account_name= account_name
    self.info_password= info_password
    self.first_name = first_name
   
   #finding info
  @classmethod
  def find_info(cls,account_name):
    """
    Find info by the name entered
    arg:
    info:the name of the info entered
    return:the name of the info entered
    """
    for credentials in cls.info_details:
     if credentials.account_name == account_name:
        
      return credentials
     
     #saving info#function
  def save_info(self):
    """
    A function that saves the app's information
    """
    Credentials.info_details.append(self)
    
    #deleting info#function
  def delete_info(self):
    """
    A function that deletes the app's information
    """
    Credentials.info_details.remove(self)
    
    #checking if the app's info exists
  def info_exists(cls,account_name):
    """
    A method that checks whether the info exists
    Args:
    info:checks whether the info exists
    returns:
    A boolean if the app's info is found
    """
    for credentials in cls.info_details:
      if credentials.account_name == account_name:
        return true
           
        return false 
  
    #display app's information
  def display_info(cls, account_name):
    """
    A method that displays the app's information
    """
    return cls.info_details
  
  
  
  @classmethod
  def find_by_first_name(cls,first_name):
     """  
      A method that finds the user using their first name
      Args:
      user: user to search for 
      returns:
      Name of the user searched for
     """
     for user in cls.info_details:
      if user.first_name == first_name:
       return user
             
  @classmethod
  def copy_credentials(cls,first_name):
    """
    method that copies credentials on the clipboard
    """
    found_credentials=cls.find_by_first_name(first_name)
    return pyperclip.copy(found_credentials.first_name)