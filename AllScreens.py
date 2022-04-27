import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from AllButtons import repeated_buttons
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget







login = None
sm= ScreenManager() 
allScreens= {}
i=0
pict= ' '
# Front end only, identifies different screens it can navigate to
class AllScreens():
    global allScreens
    global sm
    
    #------- create variable here for screen--------
    def screen(self):
    
        home = homepage(name="home")
        viewPage = view(name="view")
        viewPage2 = view(name="view2")
        viewPage3 = view(name="view3")
        viewPage4 = view(name="view4")
        viewPage5 = view(name="view5")
       

     #------- add variable here for screen to load--------
        allScreens= {
            "homeScreen" : home,
            "viewScreen1": viewPage,
            "viewScreen2": viewPage2,
            "viewScreen3": viewPage3,
            "viewScreen4": viewPage4,
            "viewScreen5": viewPage5
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


class view(Screen):
    global i
    global pict
    def pic(self):
        pict= 'price/state.png'
        return pict
    def on_click(self):
        i=0
        AllScreens.switchPageTo('homeScreen')
    pass

class view2(Screen):
    global i
    global pict
    def pic(self):
        pict= 'chartp.jpg'
        return pict 
    def on_click(self):
        i=0
        AllScreens.switchPageTo('homeScreen')
    pass
        
class view3(Screen):
    global i
    global pict
    def pic(self):
        pict= 'chartp.jpg'
        return pict       
        
        
    def on_click(self):
        i=0
        AllScreens.switchPageTo('homeScreen')
    pass

class view4(Screen):
    global i
    global pict
    def pic(self):
        pict= 'chartp.jpg'
        return pict       
        
        
    def on_click(self):
        i=0
        AllScreens.switchPageTo('homeScreen')
    pass

class view5(Screen):
    global i
    global pict
    def pic(self):
        pict= 'chartp.jpg'
        return pict       
        
        
    def on_click(self):
        i=0
        AllScreens.switchPageTo('homeScreen')
    pass

class homepage(Screen):
    # show image 1
    global i
    
    def on_click(self):
        i=1
        AllScreens.switchPageTo('viewScreen1')
        
    # show image 2
    def on_click2(self):
        i=2
        AllScreens.switchPageTo('viewScreen2')
    # show image 3
    def on_click21(self):
        i=3
        AllScreens.switchPageTo('viewScreen3')
    
    def on_click22(self):
        i=4
        AllScreens.switchPageTo('viewScreen4')
    
    def on_click23(self):
        i=5
        AllScreens.switchPageTo('viewScreen5')    
    # def process_Input(self):
    #     All_Text_Input.user_Input_search(self) 
    pass
