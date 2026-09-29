from datetime import datetime

def get_number(message, minimum, maximum):
    while True:
        number = input(message)

        if number.isdigit():
            number = int(number)

            if number >= minimum and number <= maximum:
                return number

        print("Please enter a valid number.")


def get_date():
    while True:
        date = input("Enter date (DD-MM-YYYY): ")

        try:
            d = datetime.strptime(date, "%d-%m-%Y").date()

            if d >= datetime.now().date():
                return date
            else:
                print("You cannot book a past date.")
        except:
            print("Invalid date. Please try again.")


def get_phone():
    while True:
        phone = input("Phone number: ")

        if len(phone) == 10 and phone.isdigit():
            return phone

        print("Phone number must have 10 digits.")
