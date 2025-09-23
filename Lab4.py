# Function 1: Check if the given number is a proper day number and return "It is a Weekday!" if it is, or "It is a Weekend!" if it is not.
def check_weekday_or_weekend(day_number):
    if 1 <= day_number <6:
        return "It's a Weekday."
    elif 6 <= day_number <= 7:
        return "It's a Weekend."
    else:
        return "That is not a proper day number." 
day_number=int(input("Enter day number: "))
print(check_weekday_or_weekend(day_number))
# Function 2: Check if the given number is a proper day number and return the corresponding day name.
def get_day_name(day_number):
    if day_number == 1:
        return "It's Monday"
    elif day_number == 2:
        return "It's Tuesday."
    elif day_number == 3:
        return "It's Wednesday."
    elif day_number == 4:
        return "It's Thursday."
    elif day_number == 5:
        return "It's Friday."
    elif day_number == 6:
        return "It's Saturday."
    elif day_number == 7:
        return "It's Sunday."
    else:
        return "Not a proper day number."
day_number=int(input("Enter day number: "))
print(get_day_name(day_number))