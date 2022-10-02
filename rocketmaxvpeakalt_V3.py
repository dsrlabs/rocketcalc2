# rocket-maxv-peakalt Version 3
# This program calculates the maximum (peak) altitude and velocity of a single stage
# low power model rocket, at engine burnout.
# User entered data is used for the calculation.
# Future versions may parse data from a csv file.
# Note: Rocket engine thrust data can vary by +/- 10%
import time
import datetime
print()
print('-'*77)
print("LOW POWER SINGLE STAGE MODEL ROCKET MAX. VELOCITY & PEAK ALTITUDE SIMULATION")
print("DSR Labs © 2021")
prompt = "\nPress the Enter key to continue or type 'quit' when you are finished. "
prompt += "\nIf necessary, press CTRL + z to interrupt program execution. "
print('-'*77)
# This code prints a list of rockets names in my inventory by passing it to a function called
# show_rockets
# Note: Only the inventory list is shown, The user must have the data parameters available for input.
print()
print ("DSR Labs Estes Rocket Inventory")
print()
def show_estesrocket(names):
    """Return a list of Estes low power rockets launch inventory"""
    for name in names:
        rocket_name = name.title()
        print(rocket_name)

rockets = ['1. Patriarch', '2. Dragonite', '3. Sizzler', '4. Shooting Star', '5. Skytrax', '6. Riptide', '7. Astrobeam', '8. Athena          ']
show_estesrocket(rockets)
print()
# This block of code uses a while loop to run or exit the program.
while True:
    choice = input(prompt)
    if choice == 'quit' or choice == 'QUIT':
        break
    else:
        print()
        rocketname = input("Rocket Name = ? ")
        print()
        enginetype = input("Engine type = ? ")
        print()
        while True:
            try:
                mr = float(input("Empty (no motor)rocket mass (oz) = ? "))
            except:
                print("Invalid input, please enter a number.")
                print()
            else:
                break
# Full rocket mass is:
# Empty (no motor) rocket mass (weigh or check data specs)
# Motor mass = mm (check specs or weight)
# Mass of chute and rubber band cables  - weigh this and add into eq'n)
        print()
# The following nested while loops provide input validation for an integer or float number input.
        while True:
            try:
                me = float(input("Motor mass (oz) = ? "))
            except:
                print("Invalid input, please enter a number.")
                print()
            else:
                break
        print()
        M = (mr + me)*0.0283495
        while True:
            try:
                rd = float(input("Rocket diameter (inches) = ? "))
            except:
                print("Invalid input, please enter a number.")
                print()
            else:
                break
        print()
        while True:
            try:
                T = float(input("Motor Thrust (N) = ?  "))
            except:
                print("Invalid input, please enter a number.")
                print()
            else:
                break
        print()
        while True:
            try:
                I = float(input("Motor Impulse (N-sec) = ?  "))
            except:
                print("Invalid input, please enter a number.")
                print()
            else:
                break
    # Area of the rocket is converted from inches sq. to meters sq.
        A = 3.14159*((0.5*rd)/12*0.3048)**2
        t = I/T
    # Simple calculation for the wind reistance coeefficient
        k = 0.5*1.2*0.75*A
    # Calculation of the  gravitational force (mass of the rocket times  the acceleartion of gravity
        gf = M*9.8
        import math
        a = (T - 9.8*M)/k
    # Simplification equation #2
        q = math.sqrt(a)
        x = 2*k*q/M
        vt = 1 - math.exp(-x*t)
        vb = 1 + math.exp(-x*t)
        z = vt/vb
    # The maximum velocity at engine burnout in meters per sec and in miles per hour
        v_max = q*z
        v_max_mph = v_max*2.23694
        print()
        print('-'*77)
        print("Rocket Name: " + rocketname.title())
        print()
        print(
            f"The maximum velocity at engine burnout is {v_max:.2f} m/s or {v_max_mph:.2f} mph")
# The following code block calculates the boost and phase distances, then the peak altitude post engine cutoff
        j = 2*k
        yb1 = -M/j
        yb2 = T - gf - k*v_max**2
        yb3 = T - gf
        yb = yb1*math.log(yb2/yb3)
        yb_ft = yb*3.28084
        yc1 = M/j
        yc2 = gf + k*v_max**2
        yc3 = gf
        yc = yc1*math.log(yc2/yc3)
        yc_ft = yc*3.28084
# The following block of code calculates and prints the boost and coast phase distances in feet and km.
        print(f"The boost phase distance is {yb:.2f} m or {yb_ft:.2f} ft")
        print(f"The coast phase distance is {yc:.2f} m or {yc_ft:.2f} ft")
# The following block code calculates and prints the peak altitude in meters(m) and feet(f).
        peak_alt = yb + yc
        peak_alt_ft = yb_ft + yc_ft
        print(f"The peak altitude is {peak_alt:.2f} m or {peak_alt_ft:.2f} ft")
        print('-'*77)
        print()

print()
print('-'*31)
print("Terminating Program - Goodbye.")
now_date = datetime.date.today()
now_now = time.strftime("%H:%M %p")
print(f"Date: {now_date}\nTime: {now_now}")
print('-'*31)
print()