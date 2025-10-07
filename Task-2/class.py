class Rectangle:
    def __init__(self,length=0,width=0):
        self.length =length 
        self.width = width  
    def __iter__(self):
        yield {'length':self.length}
        yield {"width": self.width}


Rect = Rectangle(20,30)

for i in Rect:
    print(i)