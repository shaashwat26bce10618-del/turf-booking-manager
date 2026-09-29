import random
from data import bookings, SLOTS

def make_id():
    number = random.randint(1000, 9999)

    while True:
        found = False

        for booking in bookings:
            if booking["id"] == number:
                found = True

        if found:
            number = random.randint(1000, 9999)
        else:
            return number


def get_taken_slots(turf, date):
    taken = []

    for booking in bookings:
        if booking["turf_id"] == turf and booking["date"] == date:
            taken.append(booking["slot"])

    return taken


def add_booking(turf, date, slot, name, phone, turf_name, price):
    booking = {
        "id": make_id(),
        "name": name,
        "phone": phone,
        "turf_id": turf,
        "turf": turf_name,
        "date": date,
        "slot": slot,
        "amount": price
    }

    bookings.append(booking)
    return booking


def cancel_booking_by_id(booking_id):
    for booking in bookings:
        if booking["id"] == booking_id:
            bookings.remove(booking)
            return booking

    return None
