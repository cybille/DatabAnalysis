import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from AllButtons import repeated_buttons
from AllTextInput import All_Text_Input
from AllDisplay import Template
from AllDisplay import AllDisplay
import apiAccessor



login = None
sm= ScreenManager() 
allScreens= {}
# Front end only, identifies different screens it can navigate to
class AllScreens():
    global allScreens
    global sm
    #------- create variable here for screen--------
    def screen(self):
        signIn= sign_in_screen(name="signIn")
        signUp= sign_up_screen(name="signUp")
        home = homepage(name="home")

        viewAccount= view_account(name="viewAccount")
        searchS= search(name="search")
        myBooking= my_booking(name="myBooking")

        joinLoyalty= join_loyalty(name="joinLoyalty")
        loyaltyRewards= loyalty_and_rewards(name="loyaltyRewards")

        viewPersonalInfo= view_personalinfo(name="viewPersonalInfo")
        viewSecurity= view_security(name="viewSecurity")
        payment= payment_Info(name="payment")
        viewBooking= view_booking(name = "viewBooking")
     #------- add variable here for screen to load--------
        allScreens= {
            "signInScreen" : signIn,
            "signUpScreen" : signUp,
            "homeScreen" : home,
            "viewAccountScreen" : viewAccount,
            "searchScreen" : searchS,
            "myBookingScreen" : myBooking,
            "joinLoyaltyScreen" : joinLoyalty,
            "loyaltyRewardsScreen" : loyaltyRewards,
            "personalInfoScreen" : viewPersonalInfo,
            "securityScreen" : viewSecurity,
            "paymentScreen" : payment,
            "viewBookingScreen" : viewBooking,
        }
        return allScreens

    def create(self):
        screens= AllScreens().screen()
        for pages in screens:
            sm.add_widget(screens[pages])
        return sm

    #------- call to switch page with correct key --------
    def switchPageTo(page):
        screens= AllScreens().screen()

        # print(screens)
        # print(page)
        # print(sm.screen_names)
        print("Page should have switched")
        sm.switch_to(screens[page])


class homepage(Screen):
    def on_click(self):
        repeated_buttons().on_click_Search_Button()

    def on_click2(self):
        repeated_buttons().navigate_to_loyalty()

    def on_click21(self):
        repeated_buttons().navigate_to_account()
    
    def on_click22(self):
        repeated_buttons().navigate_to_homepage()
    
    def on_click23(self):
        repeated_buttons().navigate_to_Search()
    
    def process_Input(self):
        All_Text_Input.user_Input_search(self) 
    pass
