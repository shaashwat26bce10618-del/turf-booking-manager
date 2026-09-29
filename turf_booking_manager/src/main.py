from data import TURFS, SLOTS, bookings
from validation import get_number, get_date, get_phone
from booking import get_taken_slots, add_booking, cancel_booking_by_id
from display import show_turfs, show_slots, print_booking, show_menu
from reports import view_bookings, search_bookings, recent_bookings, show_summary


def check_availability():
    show_turfs()
    turf = get_number("Choose turf: ", 1, 3)
    date = get_date()
    taken = get_taken_slots(turf, date)
    show_slots(turf, date, taken)


def book_slot():
    show_turfs()

    turf = get_number("Choose turf: ", 1, 3)
    date = get_date()
    taken = get_taken_slots(turf, date)

    show_slots(turf, date, taken)

    if len(taken) == len(SLOTS):
        print("Sorry, all slots are booked.")
        return

    while True:
        choice = get_number("Choose slot number: ", 1, 8)
        slot = SLOTS[choice - 1]

        if slot not in taken:
            break

        print("That slot is already booked. Choose another one.")

    name = input("Customer name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    phone = get_phone()
    turf_name = TURFS[turf][0]
    price = TURFS[turf][1]

    booking = add_booking(turf, date, slot, name, phone, turf_name, price)

    print("\nBooking confirmed!")
    print("Booking ID:", booking["id"])
    print("Name:", name)
    print("Turf:", turf_name)
    print("Date:", date)
    print("Slot:", slot)
    print("Amount: Rs.", price)


def cancel_booking():
    if len(bookings) == 0:
        print("\nNo bookings to cancel.")
        return

    value = input("Enter booking ID to cancel: ")

    if not value.isdigit():
        print("Booking ID must be a number.")
        return

    removed = cancel_booking_by_id(int(value))

    if removed:
        print("Booking", value, "has been cancelled.")
    else:
        print("No booking found with that ID.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            check_availability()
        elif choice == "2":
            book_slot()
        elif choice == "3":
            view_bookings()
        elif choice == "4":
            search_bookings()
        elif choice == "5":
            cancel_booking()
        elif choice == "6":
            recent_bookings()
        elif choice == "7":
            show_summary()
        elif choice == "8":
            print("Thank you for using Turf Booking Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Select a number from 1 to 8.")


main()
