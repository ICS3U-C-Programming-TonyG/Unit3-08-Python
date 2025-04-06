#!/usr/bin/env python3

# Created By: Tony G

# Date: 2025-04-04

# Leap year program (nested if)


def main():
    # Try catch
    try:
        year = int(input("Enter a year: "))
    # Nested if statements
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print(f"{year} is a leap year.")
                else:
                    print(f"{year} is not a leap year.")
            else:
                print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    # Try catch exception
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
