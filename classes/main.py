
# python3 main.py

from shapes import Rectangle, Square, Cube, Prism

rect = Rectangle(3,4)
print(f"length : {rect.length}")
print(f"area: {rect.area()}")
print(f"perimeter: {rect.perimeter()}")
print(rect.shape_name())

print('------------------------------------------------------------')

s = Square(2)
print(f"length : {s.length}")
print(f"area: {s.area()}")
print(f"perimeter: {s.perimeter()}")
print(s.shape_name())

print('------------------------------------------------------------')

c = Cube(3)
print(f"c.surface_area(): {c.surface_area()}")
print(f"c.volume(): {c.volume()}")
print(c.shape_name())

print('------------------------------------------------------------')

#? If you call super(class_name, object).method_name() you will call the method of that particular class
print(super(Cube, c).shape_name()) 
#o/p: I'm a Square
print(super(Square, c).shape_name()) 
#o/p:  I'm a Rectangle

#! If you call the super method on a class with no parent, it will throw error 
# print(super(Rectangle, c).shape_name()) 
#o/p: AttributeError: 'super' object has no attribute 'shape_name'
#? Python looks at the current object to see if a method with the name called exists. If so, great, it calls it.
#? If it doesn’t, it goes up to the parent of that object to see if there’s a method with that same name. 
#? It keeps doing this until it either finds it and calls it, or it runs out of inheritance chain. 
#? If it runs out of inheritance chain, it throws an AttributeError. 



prism = Prism(4, 7)
print(super(Prism, prism).shape_name())
#o/p: I'm a Triangle
#? It gives Triangle since it returns the first parent to be inherited 
