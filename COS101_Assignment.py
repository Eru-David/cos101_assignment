print('Mathematics & physics Operation')
#introduction
first_Name = input('First Name:   ')
last_Name = input('Last Name:    ')

start_viewwing_formulars = input('Start Viewing Formulars: ')
#area of a square
def area_of_square():
    length1 = int(input('Enter the number: '))
    length2 = int(input('Enter the number: '))
    area = length1 * length2
    print(area)
#area of a triangle
def area_of_triangle():
    height = int(input('enter a number   '))
    breath = int(input('enter a number   '))
    area_2 = '1/2' * height * breath
    print(area_2)
#area of a rectangle
def area_of_rectangle():
    height = int(input('enter a number   '))
    breath = int(input('enter a number   '))
    area_3 = breath * height
    print(area_3)
#formula for speed
def speed_formula():
    distance = int(input('enter the distance   '))
    time = int(input('enter the time   '))
    speed = distance/time
    print(speed)
#formula for energy
def energy_formula():
    power = int(input('enter the power  '))
    time = int(input('enter the time  '))
    energy = power * time
    print(energy)

options = input("enter a letter   ")

if options == "a":
    area_of_square()
elif options == 'b':
    area_of_triangle()
elif options == 'c':
    area_of_rectangle()
elif options == 'd':
    speed_formula()
elif options == 'e':
    energy_formula()
else:
    print('letter is invalid')