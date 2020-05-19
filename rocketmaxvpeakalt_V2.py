# rocket-maxv-peakalt Version 1
# This program calculates the maximum (peak) altitude and velocity of a single stage
# low power model rocket, at engine burnout.
# User entered data is used for the calculation. 
# Future versions will parse data from a csv file.
# Note: Rocket engine thrust data can vary by +/- 10%
print()
print('-'*77)
print("LOW POWER SINGLE STAGE MODEL ROCKET MAX. ALTITUDE & MAX. VELOCITY CALCULATION")
print ("DSR Labs © 2019")
prompt =  "\nPress the Enter key to continue or type 'quit' when you are finished. "
print('-'*77)
# This block of code uses a while loop to run or exit the program.
while True:
    choice = input(prompt)
    if choice == 'quit':
        break
    print()
    rocketname = input("Rocket Name = ? ")
    print()
    enginetype = input("Engine type = ? ")
    print()
    mr = float(input("Empty [no motor] rocket mass (oz) = ? "))
# Full rocket mass is:
# Empty (no motor) rocket mass (weigh or check data specs)
# Motor mass = mm (check specs or weight
# Mass of chute and rubber band cables  - weigh this and add into eq'n)
    print()
    me = float(input("Motor mass (oz) = ? "))
    print()
    M  = (mr + me)*0.0283495
    rd = float(input("Rocket diameter (inches) = ? " ))
    print()
    T = float(input("Motor Thrust (N) = ?  " )) #see data sheets
    print()
    I = float(input("Motor Impulse (N-sec) = ?  " )) #see data sheets
    #Area of the rocket is converted from inches sq. to meters sq.
    A = 3.14159*((0.5*rd)/12*0.3048)**2 
    t = I/T
    #Simple calculation for the wind reistance coeefficient
    k = 0.5*1.2*0.75*A 
    #Calculation of the  gravitational force (mass of the rocket times  the acceleartion of gravity
    gf = M*9.8 
    import math
    a = (T - 9.8*M)/k
    #Simplification equation #2
    q = math.sqrt(a)
    x = 2*k*q/M 
    vt = 1 - math.exp(-x*t)
    vb = 1 + math.exp(-x*t)
    z = vt/vb
    #The maximum velocity at engine burnout in meters per sec and in miles per hour
    v_max = q*z 
    v_max_mph = v_max*2.23694 
    print()
    print('-'*77)
    print("Rocket Name: " + rocketname.title())
    print()
    print(f"The maximum velocity at engine burnout is {v_max:.2f} m/s or {v_max_mph:.2f} mph")
#The following code block calculates the boost and phase distances, then the peak altitude post engine cutoff
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
# The following block code calculates and prints the peak altitude in feet and km.
    peak_alt = yb + yc
    peak_alt_ft = yb_ft + yc_ft
    print(f"The peak altitude is {peak_alt:.2f} m or {peak_alt_ft:.2f} ft")
    print('-'*77)
    print()

print()
print('-'*19)
print("Terminating Program")
import datetime
import time
now_date = datetime.date.today()
now_now = time.strftime("%H:%M %p")
print(f"Date: {now_date}\nTime: {now_now}")
print('-'*19)
print()