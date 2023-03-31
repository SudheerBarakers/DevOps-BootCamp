
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minute":
        return f"{num_of_days} days are {num_of_days * 24*60} minutes"
    else:
        return "Unsupported Units"


def validate_and_execute():
    try:
        user_input_num = int(days_and_unit_dictionary["days"])
        if user_input_num > 0:
            num_of_units = days_to_units(user_input_num, days_and_unit_dictionary["unit"])
            print(num_of_units)
        elif user_input_num == 0:
            print("You enter 0")
        else:
            print("You entered negative number")

    except ValueError:
        print("Your input is not a valida number!")


user_input = ""
while user_input != "exit":
    user_input = input("User, enter number of days and conversion unit\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)

    validate_and_execute()


# while True:
#     user_input = input("Enter number of days\n")
#     validate_and_execute()


