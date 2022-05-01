import kivy
from kivy.uix.screenmanager import ScreenManager

"""

CONNECT BACKEND TO FRONT END
This is where all functions that interact with specific buttons functionality
Processes anything that does not involve text
"""
# Might not need it

class text(): 

        # Action: Anything that is supposed to happen
        
    def Topic1(self):
        Title= 'Analyzing houses under 50,000:In The United states, Regions in NY, ect'
        # \n
        return Title

    def Topic2(self):
        Title= "Price of Houses with One Bedroom: in NY with One Bedroom, SqFt Below 800"
        return Title

    def Topic3(self):
        Title= "Price of Houses Below $50,000: That Allows Cats and Dogs, Doesn't Allow Pets"
        return Title

    def Topic4(self):
        Title= "Type of housing in NYC under $50,00 with parking option: carport, attached, ect"


        return Title
    
    def Topic5(self):
        Title= "Type of housing in New York with prices under $50,000 with wheelchair accessibility"
        return Title
    

    def Topic1D(self):
        Title= " Filtered for: price<50,000 \n Filtered for state= ny \n Filtered for region= new york city \n The x axis= filtered, y axis= price"
        return Title

    def Topic2D(self):
        Title= " Filtered for: price<50,000, beds==1 \n Filtered for state= ny,region= new york city, bed==1 \n Filtered for state= ny,region= new york city, bed==1, sqfeet<=800 \n The x axis= filtered, y axis= price"

        return Title

    def Topic3D(self):
        Title= " Filtered for: price<50,000, cats_allowed==1, dogs_allowed==1 \n Filtered for:state= ny,region= new york city, cats_allowed==1, dogs_allowed==1 \n Filtered for:state= ny,region= new york city, cats_allowed==0, dogs_allowed==0 \n The x axis= filtered, y axis= price"
        return Title

    def Topic4D(self):
        Title= " Filtered for: price <$50,000, ==1 \n Filtered for type = ny, region = new york city, \n parking option = carport, attached garage, detached garage, off-street parking\n X-axis = filtered, Y-axis = price"

        return Title
    
    def Topic5D(self):
        Title= " Filtered price <50,000, wheelchair accessibility == 1 \n Filtered Type, region = new york city, wheelchair_access == 1 \n X-axis = filtered, y-axis = price under $50,000"

        return Title






   
    
    

        

    