#ex.1 Calculate area geometry
import math
height, width = map(float,input("Enter hight and width (cm): ").split())

Circle_area = math.pi * height**2
Triangle_area = 1/2*width*height
Square_area = width*height
Rectangle_area = width*width

print(f"Circle area = {Circle_area: .1f} cm^2")
print(f"Triangle area = {Triangle_area: .3f} cm^2")
print(f"Square area = {Square_area: .4f} cm^2")
print(f"Tectangle area = {Rectangle_area: .4f} cm^2")

#ex.2


