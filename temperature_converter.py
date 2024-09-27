# Introduction
print("\033[93m\033[1m--------------------------------TEMPERATURE CONVERTER--------------------------------\033[0m")
print("- Conversion Type: Celsius to Fahrenheit (C to F) or Fahrenheit to Celsius (F to C) -")
print("-------------------------------------------------------------------------------------")
print()

# Ask the user if they wish to continue
start = input("\033[31m\033[1mDo you wish to continue? \033[0m(y/n): ").lower()
print()

if start == "y":  # If user wants to continue
    while True:  # Loop for multiple conversions
        # Prompt for temperature input
        print("-------------------------------------------------------------")
        temperature = input("\033[93m\033[1mEnter a temperature: \033[0m")

        # Check if the input is a valid numeric value
        if not temperature.replace('.', '', 1).isdigit():
            print("\033[31m\033[1mInvalid input. Please enter a numeric value.\033[0m")
            continue  # Restart the loop for valid input
        print(f"Temperature: {temperature}")
        print("-------------------------------------------------------------")
        # Prompt for conversion type
        print("\033[93mChoose your conversion type \033[0m")
        print("\033[1mA)\033[0m \033[94mC\033[0m to \033[95mF\033[0m")  # C to F
        print("\033[1mB)\033[0m \033[95mF\033[0m to \033[94mC\033[0m")  # F to C
        type = input("\033[1mChoose \033[1mA\033[0m or \033[1m\033[1mB: \033[0m").lower()
        print("-------------------------------------------------------------")

        # Conversion from Celsius to Fahrenheit
        if type == "a":
            celsius = float(temperature)  # Convert input to float
            fahrenheit = (9 / 5) * celsius + 32  # Calculate Fahrenheit
            print("\033[93m\033[1mConverted Temperature:\033[0m")
            print(f"\033[94m\033[4m{celsius}°C\033[0m is equal to \033[95m\033[4m{fahrenheit}°F\033[0m")
            print("-------------------------------------------------------------")
        # Conversion from Fahrenheit to Celsius
        elif type == "b":
            fahrenheit = float(temperature)  # Convert input to float
            celsius = (fahrenheit - 32) * (5 / 9)  # Calculate Celsius
            print("\033[93m\033[1mConverted Temperature:\033[0m")
            print(f"\033[95m\033[4m{fahrenheit}°F\033[0m is equal to \033[94m\033[4m{celsius}°C\033[0m")
            print("-------------------------------------------------------------")
        else:
            print("Invalid choice. Please select A or B only.")  # Handle invalid choice
            print("-------------------------------------------------------------")
        # Ask if the user wants to convert another temperature
        print()
        loop = input("\033[31m\033[1mDo you want to convert another temperature? \033[0m(y/n): ").lower()
        print()

        if loop != "y":
            print("-------------------------------------------------------------")
            print("End of program. Thank you.")
            print("-------------------------------------------------------------")
            print()
            break  # Exit the loop and program

# If user chooses not to continue
elif start == "n":
    retry = input("\033[31m\033[1mDo you want to start over? \033[0m(y/n): ").lower()
    if retry != "y":
        print("-------------------------------------------------------------")
        print("End of program. Thank you.")  # Exit program
        print("-------------------------------------------------------------")
        print()
# Handle invalid initial input
else:
    print("Invalid input. Please enter only 'y' or 'n'.")
    print("-------------------------------------------------------------")
    print()

