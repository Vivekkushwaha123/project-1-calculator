FACTORS = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462,
}


# Ask the user for a number until they type a valid one
def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number, for example 12 or 3.5.")


# ---------- Arithmetic functions ----------

# Add two numbers
def add(a, b):
    return a + b


# Subtract b from a
def subtract(a, b):
    return a - b


# Multiply two numbers
def multiply(a, b):
    return a * b


# Divide a by b, with a friendly message for zero
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


# ---------- Unit conversion functions ----------

# Convert kilometres to miles
def km_to_miles(km):
    return km * FACTORS["km_to_miles"]


# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


# Convert kilograms to pounds
def kg_to_pounds(kg):
    return kg * FACTORS["kg_to_pounds"]


# ---------- Menus ----------

# Show the unit conversion sub-menu and run the chosen conversion
def convert_units_menu():
    print("\nUnit conversions:")
    print("1) Kilometres to miles")
    print("2) Celsius to Fahrenheit")
    print("3) Kilograms to pounds")
    print("4) Back to main menu")
    choice = input("Choose a conversion: ").strip()

    if choice == "1":
        km = read_number("Kilometres: ")
        print("Result:", round(km_to_miles(km), 2), "miles")
    elif choice == "2":
        c = read_number("Celsius: ")
        print("Result:", round(celsius_to_fahrenheit(c), 2), "F")
    elif choice == "3":
        kg = read_number("Kilograms: ")
        print("Result:", round(kg_to_pounds(kg), 2), "pounds")
    elif choice == "4":
        return
    else:
        print("Please pick a number from 1 to 4.")


# Run arithmetic for menu options 1 to 4
def do_arithmetic(choice):
    a = read_number("First number: ")
    b = read_number("Second number: ")

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    else:
        print("Result:", divide(a, b))


# Main program: show the menu again and again until the user quits
def main():
    while True:
        print("\n===== Calculator & Unit Converter =====")
        print("1) Add")
        print("2) Subtract")
        print("3) Multiply")
        print("4) Divide")
        print("5) Convert units")
        print("6) Quit")
        choice = input("Choose an option: ").strip()

        if choice == "6":
            print("Goodbye!")
            break
        elif choice in ("1", "2", "3", "4"):
            do_arithmetic(choice)
        elif choice == "5":
            convert_units_menu()
        else:
            print("Please pick a number from 1 to 6.")


if __name__ == "__main__":
    main()