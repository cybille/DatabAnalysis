import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from AllButtons import repeated_buttons





login = None
sm= ScreenManager() 
allScreens= {}
# Front end only, identifies different screens it can navigate to
class AllScreens():
    global allScreens
    global sm
    #------- create variable here for screen--------
    def screen(self):
    
        home = homepage(name="home")

     #------- add variable here for screen to load--------
        allScreens= {
            "homeScreen" : home
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
    # show image
    def on_click(self):
        repeated_buttons().on_click_Search_Button()
    # show image 2
    def on_click2(self):
        repeated_buttons().navigate_to_loyalty()
    # show image 3
    def on_click21(self):
        repeated_buttons().navigate_to_account()
    
    def on_click22(self):
        repeated_buttons().navigate_to_homepage()
    
    def on_click23(self):
        repeated_buttons().navigate_to_Search()
    
    # def process_Input(self):
    #     All_Text_Input.user_Input_search(self) 
    pass
