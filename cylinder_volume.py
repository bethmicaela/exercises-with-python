introduction = """\nFind the volume of a cylinder\n"""
print(introduction)

radius = (int(input("Enter radius: ")))
height = (int(input("Enter height: ")))

def cylinder(r2, h):
    
    pi = (float(3.14))
    r2 = radius **2
    h = height

    volume = pi * r2 * h
    print("The volume of the cylinder is:", round(volume, 1), "cm3")

if __name__ == "__main__":
    cylinder(radius, height)