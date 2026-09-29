from data import TURFS, SLOTS

def show_turfs():
    print("\nAvailable Turfs")
    print("--------------------")

    for number in TURFS:
        print(number, ".", TURFS[number][0], "- Rs.", TURFS[number][1], "per hour")


def show_slots(turf, date, taken):
    print("\nSlots on", date)
    print("--------------------")

    number = 1

    for slot in SLOTS:
        if slot in taken:
            print(number, ".", slot, "- Booked")
        else:
            print(number, ".", slot, "- Free")

        number = number + 1


def print_booking(booking):
    print(
        booking["id"], "|",
        booking["name"], "|",
        booking["turf"], "|",
        booking["date"], "|",
        booking["slot"], "| Rs.",
        booking["amount"]
    )


def show_menu():
    print("\n===== TURF BOOKING MANAGER =====")
    print("1. Check availability")
    print("2. Book a slot")
    print("3. View all bookings")
    print("4. Search booking")
    print("5. Cancel booking")
    print("6. Latest bookings")
    print("7. Summary")
    print("8. Exit")
