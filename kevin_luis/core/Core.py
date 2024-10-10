import os
import importlib
from kevin_luis.config import APP_PATH

"""
    Class responsible for opening controllers
"""
class Core:   
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        Given a controllers name, return an instance of it
    
        @param controllers:string controllers to be opened
    """
    @staticmethod
    def openController(controller):
        response = None

        # Set controllers name
        controller = controller[0].upper()+controller[1:]
        controllerName = controller+"controllers"
        
        # Check if file exists
        if os.path.exists(APP_PATH+"/controllers/"+controllerName+".py"):
            module = importlib.import_module("controllers."+controllerName)
            class_ = getattr(module, controllerName)
            response = class_()
        
        return response