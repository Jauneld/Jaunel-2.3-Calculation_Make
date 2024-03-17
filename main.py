#Jaunel Deans
#Septemeber 29, 2023

name = input("Hello user, what is your name? ")
print("Nice to meet you " + name + ".")

# Get input for length & width. Convert to integers and store in variables
length1 = int(input("Please enter the length of the rectangle: "))
width1 = int(input("Please enter the width of the rectangle: "))
# Calculate the area & store the result in the area variable
area = length1 * width1
# Output the area variable (converted to string)
print(name, "the area of the rectangle is", str(area) + ".")
print("     ", width1)
print(">  _________")
print("> |         |")
print("> |         | ", length1)
print("> |_________|")
print(">  Area = ", area)

#1
print()
# Get input for length & width. Convert to integers and store in variables
length2 = int(input("Please enter the length of the rectangle: "))
width2 = int(input("Please enter the width of the rectangle: "))
# Calculate the perimeter & store the result in the peri variable
peri = (length2 + width2) * 2
# Output the peri variable (converted to string)
print(name, "the perimeter of the rectangle is", str(peri) + ".")
print("     ", width2)
print(">  _________")
print("> |         |")
print("> |         | ", length2)
print("> |_________|")
print(">  Perimeter = ", peri)

#2
print()
firstPrice = float(input("Enter to cost of your meal: $"))
tip = (firstPrice * .20)
totalCost = firstPrice + tip
print(name + ", the tip price is $" + str(tip),
      "and the total cost is $" + str(totalCost))

#3
print()
length3 = int(input("Please enter the length of the cuboid: "))
width3 = int(input("Please enter the width of the cuboid: "))
height3 = int(input("Please enter the height of the cuboid: "))
volume = (length3 * width3 * height3)
print(name, "the volume of the cubiod is", str(volume) + ".")
