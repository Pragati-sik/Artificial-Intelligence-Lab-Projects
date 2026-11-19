
# SMART IRRIGATION DECISION SYSTEM
# Artificial Intelligence Lab Project
# Concepts: Expert System, Facts, Rules and Reasoning

import math


# Function to accept and validate numerical input
def get_input(message, minimum, maximum):

    while True:
        try:
            value = float(input(message))

            # Check for NaN and infinity
            if not math.isfinite(value):
                print("Error: Please enter a valid finite number.")
                continue

            # Check allowed range
            if value < minimum or value > maximum:
                print("Error: Value must be between",
                      minimum, "and", maximum)
                continue

            return value

        except ValueError:
            print("Invalid input! Please enter numbers only.")


# Function to select crop
def select_crop():

    print("\nSelect Crop Type:")
    print("1. Rice")
    print("2. Wheat")

    while True:
        try:
            choice = int(input("Enter your choice (1 or 2): "))

            if choice == 1:
                return "Rice", 60

            elif choice == 2:
                return "Wheat", 40

            else:
                print("Invalid choice! Please select 1 or 2.")

        except ValueError:
            print("Invalid input! Enter an integer.")


# Expert system decision-making function
def irrigation_decision(moisture, temperature,
                        humidity, rainfall, required_moisture):

    # Rule 1: Sufficient rainfall
    if rainfall >= 10:
        return "NO IRRIGATION", "Sufficient rainfall is available."

    target = required_moisture

    # Rule 2: High temperature increases water requirement
    if temperature >= 35:
        target += 5

    # Rule 3: Low humidity increases water requirement
    if humidity < 35:
        target += 5

    # Rule 4: High humidity reduces water requirement
    if humidity >= 80:
        target -= 5

    # Rule 5: Moderate rainfall reduces water requirement
    if rainfall >= 2:
        target -= 5

    # Calculate moisture deficit
    deficit = target - moisture

    # Final irrigation rules
    if deficit <= 0:
        return "NO IRRIGATION", "Soil moisture is sufficient."

    elif deficit <= 10:
        return "LOW IRRIGATION", "Soil moisture is slightly low."

    elif deficit <= 25:
        return "MEDIUM IRRIGATION", "Soil needs a moderate amount of water."

    else:
        return "HIGH IRRIGATION", "Soil moisture is very low."


# Main program
def main():

    print("\n======================================")
    print("       SMART IRRIGATION SYSTEM")
    print("======================================")

    while True:

        # Accept environmental conditions
        print("\nEnter Field Conditions:")

        moisture = get_input(
            "Enter soil moisture (0-100%): ", 0, 100)

        temperature = get_input(
            "Enter temperature (-10 to 60 C): ", -10, 60)

        humidity = get_input(
            "Enter humidity (0-100%): ", 0, 100)

        rainfall = get_input(
            "Enter rainfall (0-1000 mm): ", 0, 1000)

        # Select crop
        crop_name, required_moisture = select_crop()

        # Display field details
        print("\n========== FIELD CONDITIONS ==========")

        print("Crop Type:", crop_name)
        print("Soil Moisture:", moisture, "%")
        print("Temperature:", temperature, "C")
        print("Humidity:", humidity, "%")
        print("Rainfall:", rainfall, "mm")

        # Get irrigation recommendation
        decision, reason = irrigation_decision(
            moisture,
            temperature,
            humidity,
            rainfall,
            required_moisture
        )

        # Display result
        print("\n========== IRRIGATION RESULT ==========")

        print("Recommended Action:", decision)
        print("Reason:", reason)

        print("\n======================================")

        # Ask user whether to continue
        while True:
            try:
                again = input(
                    "\nDo you want to check another field? (yes/no): "
                ).strip().lower()

                if again in ["yes", "y"]:
                    break

                elif again in ["no", "n"]:
                    print("\nThank you for using Smart Irrigation System!")
                    return

                else:
                    print("Please enter yes or no.")

            except (EOFError, KeyboardInterrupt):
                print("\nProgram stopped.")
                return


# Program execution with exception handling
if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")

    except EOFError:
        print("\nInput ended. Program terminated.") 
