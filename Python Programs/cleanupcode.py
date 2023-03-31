calculation_to_seconds = 20
unit_of_days = "seconds"


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days*calculation_to_seconds} {unit_of_days}"
    elif num_of_days == 0:
        return "You enter 0"


def validate_and_execute():
    if user_input.isdigit():
        num_of_units = days_to_units(int(user_input))
        print(num_of_units)
    else:
        print("Your input is not a valida number!")


user_input = input("Enter number of days\n")
validate_and_execute()


