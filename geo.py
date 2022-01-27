#Exercice1
class square():
    def __init__(self, length):
	self.length = length
	
    @property
    def center(self):
    	pass
    	
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
		super(rectangle,self)._init_(self.length)
        def area(self):
            return self.length * self.width
        def perimeter(self):
            return 2*(self.length+self.width)
        pass
        
class position():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        pass
        

