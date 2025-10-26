import math
def volume_of_cylinder(radius,height):
    volume=math.pi * radius**2 * height
    return volume
r=float(input("Enter the radius of the cylinder: "))
h=float(input("Enter the height of the cylinder: "))
v = volume_of_cylinder(r,h)
print(f"The volume of the cylinder is:{v:.2f}")
