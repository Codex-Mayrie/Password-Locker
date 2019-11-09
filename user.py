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
    def find_by_firstname(cls,first_name):
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
    
    #checking if the user exists
    def user_exists(cls, first_name):
      """
      A method that checks whether the user exists
      Args:
        user:checks whether the user exists using the first name
        returns:
        A boolean if the user is found using the first name
        """
      for user in cls.user_details:
          if user.first_name == first_name:
           return true
           return false
         
    #displaying user
    def display_user(cls):
     """
      A function that displays the user
     """
    return cls.user_details()
    