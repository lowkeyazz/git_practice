#Exercice1
class square():
    def __init__(self, length):
        self.length = length
    def area(self):
        return (self.length**2)
    def perimeter(self):
        return (self.length*4)
    pass
    
 #Exercice2
 class rectangle(square):
        def __init__(self, length, width):
                self.length = length
                self.width = width
        pass
