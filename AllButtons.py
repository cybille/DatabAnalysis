import AllTextInput
import kivy
from kivy.uix.screenmanager import ScreenManager
import AllScreens
"""

CONNECT BACKEND TO FRONT END
This is where all functions that interact with specific buttons functionality
Processes anything that does not involve text
"""

class repeated_buttons(): 

        # Action: Anything that is supposed to happen
    def on_click_Join_Loyalty(self):
        print("Joined Loyalty")
    def on_click_Submit_Booking(self):
        print("Submitted Booking")
    def on_click_Search_Button(self):
        print("Searching...")
    def on_click_sign_in(self):
        print("Signed In")





    def on_click_Sign_up(self):
        print("Signed Up")
    def on_click_Submit_Personal_Info(self):
        print("Submitted Personal Info")
    def on_click_Submit_Payment(self):
        print("Submitted Payment")

        # Navigate: Changing screen or redirecting to something
    def navigate_to_account(self):
        print("to Account Page")
    def navigate_to_homepage(self):
        

        print("to Search page")
    def navigate_to_Booking(self):
        print("to Booking page")
    def navigate_to_loyalty(self):
        print("to Loyalty page")
    def navigate_to_Payment(self):
        print("to Payment Page")
    def navigate_to_Search(self):
        print("to Search page")
    def navigate_to_Secutiy(self):
        print("to security page")
    def navigate_to_sign_in(self):
        print("to sign in page")

       
            

    





    def navigate_to_sign_up(self):
        print("to sign up page")
   
    
    

        

    