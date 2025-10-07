## Custom Classes in Pyhon
Here we see a class created Rectangle as seen
``` bash 
class Rectangle:
    def __init__(self,length=0,width=0):
        self.length =length 
        self.width = width  
    def __iter__(self):
        yield {'length':self.length}
        yield {"width": self.width}
```
__init__ intialize a length and width
__iter__ itterates an instance of Rectangle class
