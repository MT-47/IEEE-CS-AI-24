def number_validation():
    try:
        x = int(input("Please enter a number: "))
        print("You entered:", x)
    except ValueError:
        print("it's not a numeric value.")
        number_validation()

number_validation()
