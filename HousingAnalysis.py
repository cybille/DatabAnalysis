
import kivy
import kivymd
from kivymd.app import MDApp
from kivy.app import App
from AllTemplates import AllTemplates
from AllScreens import AllScreens
  
#Load all screens and layouts
AllScreens()


# loads all templates
AllTemplates().loadTemplates()

# load screen manager .kv file
class Fre_Hotels():
    pass

class Fre_Hotels_Run(MDApp):
    def build(self):
        self.title = "FRE Hotel"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return AllScreens.create(self)

#runs application

Fre_Hotels_Run().run()
