from data import bookings
from display import print_booking

def view_bookings():
    if len(bookings) == 0:
        print("\nNo bookings yet.")
        return

    print("\nAll Bookings")
    print("--------------------")

    for booking in bookings:
        print_booking(booking)


def search_bookings():
    if len(bookings) == 0:
        print("\nNo bookings yet.")
        return

    search = input("Enter customer name or phone: ").lower()
    found = 0

    for booking in bookings:
        name = booking["name"].lower()
        phone = booking["phone"]

        if search in name or search == phone:
            print_booking(booking)
            found = found + 1

    if found == 0:
        print("No matching booking found.")
    else:
        print(found, "booking(s) found.")


def recent_bookings():
    if len(bookings) == 0:
        print("\nNo bookings yet.")
        return

    print("\nLatest Bookings")
    print("--------------------")

    start = len(bookings) - 1
    count = 0

    while start >= 0 and count < 5:
        print_booking(bookings[start])
        start = start - 1
        count = count + 1


def show_summary():
    if len(bookings) == 0:
        print("\nNo bookings yet.")
        return

    total = 0
    customers = []
    football = 0
    cricket = 0
    box_cricket = 0
    highest = bookings[0]

    for booking in bookings:
        total = total + booking["amount"]

        if booking["phone"] not in customers:
            customers.append(booking["phone"])

        if booking["turf"] == "Football Turf":
            football = football + 1
        elif booking["turf"] == "Cricket Turf":
            cricket = cricket + 1
        else:
            box_cricket = box_cricket + 1

        if booking["amount"] > highest["amount"]:
            highest = booking

    if football >= cricket and football >= box_cricket:
        popular = "Football Turf"
        popular_count = football
    elif cricket >= football and cricket >= box_cricket:
        popular = "Cricket Turf"
        popular_count = cricket
    else:
        popular = "Box Cricket"
        popular_count = box_cricket

    print("\nSummary")
    print("--------------------")
    print("Total bookings:", len(bookings))
    print("Total revenue: Rs.", total)
    print("Unique customers:", len(customers))
    print("Most booked turf:", popular)
    print("Bookings for it:", popular_count)
    print("Highest amount: Rs.", highest["amount"])
