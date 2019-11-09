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
       """
       A function that deletes the app's information
       """
       Credentials.info_details.remove(self)
       