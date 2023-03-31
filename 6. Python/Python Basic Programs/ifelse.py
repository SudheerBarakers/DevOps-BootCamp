calculation_to_seconds = 20
unit_of_days = "seconds"


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days*calculation_to_seconds} {unit_of_days}"
    else:
        return "Negative number"


user_input = input("Enter number of days\n")
user_input_num = int(user_input)
print(user_input)

num_of_units = days_to_units(user_input_num)
print(num_of_units)

