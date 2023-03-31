calculation_to_seconds = 20*65
unit_of_days = "seconds"


def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days*calculation_to_seconds} {unit_of_days}")


def days_to_months(months):
    return f"{months *12} to be calculated"


user_input = input("Enter number of days\n")
print(user_input)

days_to_units(30)

num_of_months = days_to_months(2)
print(num_of_months)