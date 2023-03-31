calculation_to_seconds = 20
unit_of_days = "seconds"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days*calculation_to_seconds} {unit_of_days}"


def validate_and_execute():
    if user_input.isdigit():
        user_input_num = int(user_input)
        if user_input_num > 0:
            num_of_units = days_to_units(user_input_num)
            print(num_of_units)
        else:
            user_input == 0
            print("You enter 0")
    else:
        print("Your input is not a valida number!")


user_input = input("Enter number of days\n")
validate_and_execute()


