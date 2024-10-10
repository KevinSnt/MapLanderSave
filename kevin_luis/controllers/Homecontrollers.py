from kevin_luis.core.Controller import Controller


class Homecontrollers(Controller):
    numberSystem = 'decimal'
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self):
        self.homeView = self.loadView("Home")

    def getButtonNumbers(self):
        match self.__class__.numberSystem:
            case 'decimal':
                typeNumbers = [
                    ('1', 0, 3), ('2', 0, 4), ('3', 0, 5),
                    ('4', 1, 3), ('5', 1, 4), ('6', 1, 5),
                    ('7', 2, 3), ('8', 2, 4), ('9', 2, 5),
                    ('0', 3, 3)
                ]
            case 'binary':
                typeNumbers = [
                    ('0', 0, 3), ('1', 0, 4)
                ]
            case 'octal':
                typeNumbers = [
                    ('1', 0, 3), ('2', 0, 4), ('3', 0, 5),
                    ('4', 1, 3), ('5', 1, 4), ('6', 1, 5),
                    ('7', 2, 3)
                ]
            case 'hexadecimal':
                typeNumbers = [
                    ('1', 0, 3), ('2', 0, 4), ('3', 0, 5),
                    ('4', 1, 3), ('5', 1, 4), ('6', 1, 5),
                    ('7', 2, 3), ('8', 2, 4), ('9', 2, 5),
                    ('0', 3, 3), ('A', 3, 4), ('B', 3, 5),
                    ('C', 4, 3), ('D', 4, 4), ('E', 4, 5),
                    ('F', 5, 3)
                ]
        return typeNumbers
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        @Override
    """
    def main(self):
        self.homeView.main()
