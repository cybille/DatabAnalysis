import code
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from AllButtons import repeated_buttons
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from AllText import text







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
        viewPage2 = view2(name="view2")
        viewPage3 = view3(name="view3")
        viewPage4 = view4(name="view4")
        viewPage5 = view5(name="view5")
        code = codeSource(name="codeSource")
       

     #------- add variable here for screen to load--------
        allScreens= {
            "homeScreen" : home,
            "viewScreen1": viewPage,
            "viewScreen2": viewPage2,
            "viewScreen3": viewPage3,
            "viewScreen4": viewPage4,
            "viewScreen5": viewPage5,
            "codeScreen": code

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

class codeSource(Screen):
    global i
    global pict
    def pic(self):
        pict= 'price/housesunder50instates.png'
        return pict
    def pic2(self):
        pict= 'price/state.png'
        return pict    
        
    def on_click(self):
        i=0
        AllScreens.switchPageTo('homeScreen')
    pass

class view(Screen):
    global i
    global pict
    def pic(self):
        pict= 'price/housesunder50instates.png'
        return pict
    def pic2(self):
        pict= 'price/regions inNYC price.png'
        return pict    
    def pic3(self):
        pict= 'price/typesandpriceinny.png'
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
    def pic4(self):
        pict= 'one bed/House W One Bedroom in NY.png'
        return pict   
    def pic5(self):
        pict= 'one bed/Price of Houses in NY with One Bedroom and SqFt Below 800.png'
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
    def pic7(self):
        pict= 'pets\Houses in NY without pets.png'
        return pict
    def pic8(self):
        pict= 'pets\House in NY that allow cats and dogs.png'
        return pict 
    def pic9(self):
        pict= 'pets\House below 50000 that allow cats and dogs.png'
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
    def pic10(self):
        pict= 'parking\park1.jpg'
        return pict 
    def pic11(self):
        pict= 'parking\park2.jpg'
        return pict 
    def pic12(self):
        pict= 'parking\park3.jpg'
        return pict 
    def pic13(self):
        pict= 'parking\park4.jpg'
        return pict 

    def on_click(self):
        i=0
        AllScreens.switchPageTo('homeScreen')
    pass

class view5(Screen):
    global i
    global pict
    def pic(self):
        pict= 'accessibility\wheel.jpg'
        return pict    

    def pic2(self):
        pict= 'accessibility\wheel.jpg'
        return pict    
    
    def pic3(self):
        pict= 'accessibility\wheel.jpg'
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
    
    def on_click3(self):
        i=6
        AllScreens.switchPageTo('codeScreen')

    def process_Input(self):
        search= self.ids.search.text
        print(search)
        return search
# view1
    def pic(self):
        pict= 'price/housesunder50instates.png'
        return pict
    def pic2(self):
        pict= 'price/regions inNYC price.png'
        return pict    
    def pic3(self):
        pict= 'price/typesandpriceinny.png'
        return pict  
# view2
    def pic4(self):
        pict= 'one bed/House W One Bedroom in NY.png'
        return pict   
    def pic5(self):
        pict= 'one bed/Price of Houses in NY with One Bedroom and SqFt Below 800.png'
        return pict 
    def pic6(self):
        pict= 'price/state.png'
        return pict
# view3
    def pic7(self):
        pict= 'pets\Houses in NY without pets.png'
        return pict 
    def pic8(self):
        pict= 'pets\House in NY that allow cats and dogs.png'
        return pict 
    def pic9(self):
        pict= 'pets\House below 50000 that allow cats and dogs.png'
        return pict   
# view4
    def pic10(self):
        pict= 'parking\park1.jpg'
        return pict 
    def pic11(self):
        pict= 'parking\park2.jpg'
        return pict 
    def pic12(self):
        pict= 'parking\park3.jpg'
        return pict 
    def pic13(self):
        pict= 'parking\park4.jpg'
        return pict 
# view5
    def pic14(self):
        pict= 'price/state.png'
        return pict 
    def pic15(self):
        pict= 'price/state.png'
        return pict


# Text-----------------
    def title1(self):
        return text.Topic1(self)
    def title2(self):
        return text.Topic2(self)
    def title3(self):
        return text.Topic3(self)
    def title4(self):
        return text.Topic4(self)
    def title5(self):
        return text.Topic5(self)

    def detail1(self):
        return text.Topic1D(self)
    def detail2(self):
        return text.Topic2D(self)
    def detail3(self):
        return text.Topic3D(self)
    def detail4(self):
        return text.Topic4D(self)
    def detail5(self):
        return text.Topic5D(self)
    pass