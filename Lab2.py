# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    # TODO: Implement this function
    g=9.8
    h=h0-1/2*g*t**2
    return h
    pass  # Replace with your code
h0=float(input("Enter initial height (m):"))
t=float(input("Enter time (s):"))
print(f"Height of the ball at time {t} seconds = {calculate_height(h0, t)} meters.")

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    s=20
    distance=s*t
    return distance
    pass  # Replace with your code
t=float(input("Enter time for car (in seconds):"))
print(f"the car will travel {calculate_car_distance(t)} meters in {t} seconds.")







# Hello Hanif