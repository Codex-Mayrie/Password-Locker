import random
import string

class Credentials: 
  """
  This is a class that creates new instances of user credentials
   """
  
  info_deatils= []
  
  def __init__(self, info, info_password):
   self.info= info
   self.info_password= info_password
   
   #finding info#method
  def find_info(cls,info):
     """
     Find info by the name entered
     arg:
     info:the name of the info entered
     return:the name of the info entered
     """
     for credentials in cls.info_details
     if credentials.info= info
     return info
     
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
       
      #checking if the user exists
    def info_exists(cls,info):
      """
      A method that checks whether the info exists
      Args:
        info:checks whether the info exists
        returns:
        A boolean if the app's info is found
        """
      for credentials in cls.info_details:
          if credentials.info ==info:
           return true
           return false 
       