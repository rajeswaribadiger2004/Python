def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def display_menu():
    """Display the menu options for conversion."""
    print("\nTemperature Converter")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")

def main():
    while True:
        # Display menu and get user's choice
        display_menu()
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            # Convert Celsius to Fahrenheit
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}° Celsius is equal to {fahrenheit:.2f}° Fahrenheit.")
        
        elif choice == "2":
            # Convert Fahrenheit to Celsius
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}° Fahrenheit is equal to {celsius:.2f}° Celsius.")
        
        elif choice == "3":
            print("Exiting the temperature converter. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


#OUTPUT
'''
Temperature Converter
1. Convert Celsius to Fahrenheit
2. Convert Fahrenheit to Celsius
3. Exit
Choose an option (1-3): 1
Enter temperature in Celsius: 23
23.0° Celsius is equal to 73.40° Fahrenheit.

Temperature Converter
1. Convert Celsius to Fahrenheit
2. Convert Fahrenheit to Celsius
3. Exit
Choose an option (1-3): 2
Enter temperature in Fahrenheit: 34
34.0° Fahrenheit is equal to 1.11° Celsius.

Temperature Converter
1. Convert Celsius to Fahrenheit
2. Convert Fahrenheit to Celsius
3. Exit
Choose an option (1-3): 3
Exiting the temperature converter. Goodbye!'''