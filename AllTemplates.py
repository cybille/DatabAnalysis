"""
FRONT END ONLY
load .kv files/frameworks here
"""
import kivy
from kivy.app import App
from kivy.lang import Builder


class AllTemplates():
    def loadTemplates(self):
        # Builder.load_file("name.kv")
        Builder.load_file("Homepage.kv")
        Builder.load_file("SignInPage.kv")
        Builder.load_file("SignUpPage.kv")

        Builder.load_file("CreateBooking.kv")
        Builder.load_file("Search.kv")
        Builder.load_file("ViewBooking.kv")

        Builder.load_file("JoinLoyalty.kv")
        Builder.load_file("LoyaltyAndRewards.kv")
        Builder.load_file("ViewAccount.kv")

        Builder.load_file("PersonalInfo.kv")
        Builder.load_file("ViewSecurity.kv")
        Builder.load_file("PaymentInfo.kv")


        
        