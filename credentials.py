import string
import random

class Credentials: 
  """
  This is a class that creates new instances of user credentials
   """
  
  info_credentials= []
  
  def __init__(self, info, info_password):
   self.info= info
   self.info_password= info_password