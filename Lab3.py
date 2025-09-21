import math
# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y).
def polar_to_cartesian(r, theta):
     x=(r*math.cos(theta*math.pi/180))
     y=(r*math.sin(theta*math.pi/180))
     return (round(x, 5), round(y, 5))
r=(float(input("Enter the radius: ")))
theta=((float(input("Enter angle in degrees: "))))
print(f"The Cartesian coordinates are {polar_to_cartesian(r, theta)}.")
# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ).
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x, y):
    r=(math.sqrt((x**2)+(y**2)))
    theta=((math.atan(y/x))*180/math.pi)
    return (round(r, 5), round(theta, 5))
x=float(input("Enter x: "))
y=float(input("Enter y: "))
print(f"The polar coordinates are {cartesian_to_polar(x, y)}.")
# Function 3 (40): Calculate the position of pendulum for (A, f, ϕ, t).
# This function should take (A, f, ϕ, t) as input and return the position value x.
def pendulum_position(A, f, phi, t):
    omega=2*math.pi*f
    x=A*math.cos((omega*t)+phi*math.pi/180)
    return x
A=float(input("Enter amplitude: "))
f=float(input("Enter frequency: "))
phi=float(input("Enter phase constant: "))
t=float(input("Enter time: "))
print(f"The pendulum will be displaced {pendulum_position(A, f, phi, t)} from the equilibrium point.")