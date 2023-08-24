print("Welcome to the Space Travel Calculator!")

distance = float(input("How far is the celestial object you wish to travel to, in light-years?"))

speed = float(eval(input("How fast is your spacecraft relative to the speed of light?")))

time = distance/speed

print("It would take", time, "years to reach your destination at your current speed!")

