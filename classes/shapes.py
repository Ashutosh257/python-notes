

# python3 shapes.py

#? If we want to change the functionality of a class which derives from parent class then we have to override it. 
#? Check the below link to get a better understanding 
#? https://realpython.com/python3-object-oriented-programming/#:~:text=Child%20classes%20can,parents%20don%E2%80%99t%20have.


from email.mime import base


class Rectangle:

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length + self.width)

    #! If we don't define this method in child class then both Square and Cube instances will refer to this method, unless defined   
    def shape_name(self):
        return "I'm a Rectangle"


#? we override the init method of rectangle, since our attributes are different
#? rectangle takes length and width but square only takes length 
# .super() allows us to access the parent’s methods-in this case, the parent Rectangle.__init__() method 
class Square(Rectangle):

    def __init__(self, length) -> None:
        super().__init__(length, length)

    def shape_name(self):
        return "I'm a Square"


#? here we dont have to override init method since it is similar to square 
class Cube(Square):

    def surface_area(self):
        return 6 * self.area()

    def volume(self):
        return self.length * super().area()
    
    def shape_name(self):
        return "I'm a Cube"



#- super() called within a class method gives you access to the parent object
#- super() can also be called with parameters indicating the class and object to access
#-    super(class, object)
#-    This form doesn’t even have to be inside the object method
#- Inside a class method “super()” is a shortcut for “super(my_class, self)”


class Triangle:

    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height


    def area(self):
        return 0.5 * self.base * self.height
    
    def shape_name(self):
        return "I'm a Triangle"


class Prism(Triangle, Square):

    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def what_am_i(self):
        return "I'm a Prism"


