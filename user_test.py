import unittest
from user import User
from credentials import Credentials
import pyperclip
 
class TestUser(unittest.TestCase):
  
   """
   Test case that defines the behavior that should be evident in the user class
   """
   new_user= User("Mary","Wanjiku","wanjiku254")
   new_account_name= Credentials("Instagram","Mary","wanjikuMburu254")

   def test_setUp(self):

      """
      setup method that is executed before any test case is executed
      """
      self.new_user= User("Mary","Wanjiku","wanjiku254")
      self.new_account_name= Credentials("Instagram","Mary","wanjikuMburu254")


   def test_tearDown(self):

      """
      tearDown method that clears up everything after all the tests are executed
      """
      User.user_details= []
      Credentials.info_details= []
      
      #Test to check whether the user details have been well initialized
      
   def test_init__(self):
      
      """
      A test that checks whether the object is well initialized
      """
      self.assertEqual(self.new_user.first_name,"Mary")
      self.assertEqual( self.new_user.second_name,"Wanjiku")
      self.assertEqual(self.new_user.password,"wanjiku254")
      
      self.assertEqual(self.new_account_name.account_name,"Instagram")
      self.assertEqual(self.new_account_name.info_password,"wanjikuMburu254")
      
      #Test that checks whether the user details have been saved
      
   def test_save_user(self):
      
      """
      A test that checks whether the user details have been saved
      """
      self.new_user.save_user()
      self.assertEqual(len(User.user_details),4)
   
      #Test that deletes the user's account
      
   def test_delete_user(self):  
      """
      A test that tries to check whether the user's account is deletable or deletes the user's account
      """
      self.new_user.save_user()
      test_user= User("Mary","Wanjiku","wanjiku254")
      test_user.save_user()
      
      self.new_user.delete_account()
      self.assertEqual(len(User.user_details),1)
      
      #A test that finds user by first name
   def test_find_by_first_name(self):
      """
      A test that finds user using the first name
      """
      self.new_user.save_user()
      Mary = User("Mary","Wanjiku","wanjiku254")
      Mary.save_user()
      
      found_user= User.find_by_first_name("Mary")
      self.assertEqual(found_user.first_name,"Mary")
      
   #A test that displays the user
   def test_display_user(self):
      """
      This test displays the user
      """
      self.assertEqual(User.display_user(), User.user_details)
      
    #A test that copies credentials on the clipboard  
   def test_copy_credentials(self):
      """
      Method that tests whether a user can copy credentials on the clipboard
      """
      self.new_account_name.save_info()
      Instagram=Credentials("Instagram", "Mary","wanjikuMburu254")
      Instagram.save_info()
      found_credentials=None
      for credentials in Credentials.info_details:
         found_credentials=Credentials.find_by_first_name(
            credentials.first_name)
         return pyperclip.copy(found_credentials.info_password)
      Credentials.copy_credentials(self.info_details.first_name)
      self.assertEqual("wanjikuMburu254",pyperclip.paste())
      print(pyperclip.paste())
      
          
      

if __name__ == '__main__':
    unittest.main()