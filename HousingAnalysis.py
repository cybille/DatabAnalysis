
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
# class HousingAnalysis():
#     pass

class HousingAnalysisRun(MDApp):
    def build(self):
        self.title = "Housing Analysis"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        return AllScreens.create(self)

#runs application

HousingAnalysisRun().run()
