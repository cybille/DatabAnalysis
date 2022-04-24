"""
FRONT END ONLY
load .kv files/frameworks here
"""
import kivy
from kivy.app import App
from kivy.lang import Builder


class AllTemplates():
    def loadTemplates(self):
        Builder.load_file("Homepage.kv")
        Builder.load_file("view.kv")
        Builder.load_file("view2.kv")
        Builder.load_file("view3.kv")
        Builder.load_file("view4.kv")
        Builder.load_file("view5.kv")
        # Builder.load_file("name.kv")
        
      