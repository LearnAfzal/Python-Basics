#import the class from package
from area import formula
#circle
circle_area=formula.area_of_circle(20)
print(circle_area)
print(formula.author)
print("area of circle is",formula.area_of_circle(15))
#triangle
print("area of triangle is",formula.area_of_triangle(4,5))
triangle_area=formula.area_of_triangle(4,5)
print(type(circle_area))
print(type(triangle_area))
print(circle_area+triangle_area)
#square
print("area of square is",formula.area_of_square(4))
#trapezium
print("area of trapezoid is",formula.area_of_trapezoid(5,6,7))