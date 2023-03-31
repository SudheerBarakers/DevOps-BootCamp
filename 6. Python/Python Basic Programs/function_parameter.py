calculation_to_seconds = 20*65
unit_of_days = "seconds"


def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days*calculation_to_seconds} {unit_of_days}")
    print("All are good")


days_to_units(35)
days_to_units(30)
days_to_units(20)
days_to_units(110)