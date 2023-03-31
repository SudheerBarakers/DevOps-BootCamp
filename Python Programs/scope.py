calculation_to_seconds = 20*65
unit_of_days = "seconds"


def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days*calculation_to_seconds} {unit_of_days}")


def scope_check(num_of_days):
    my_var = 300
    print(unit_of_days)
    print(num_of_days)
    print(my_var)


scope_check(20)
days_to_units(30)
