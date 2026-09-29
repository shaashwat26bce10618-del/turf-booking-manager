# Simple validation tests for the Turf Booking Manager

from data import bookings
from booking import add_booking, get_taken_slots, cancel_booking_by_id

def test_booking():
    bookings.clear()

    booking = add_booking(
        1,
        "30-09-2026",
        "06:00-07:00",
        "Test User",
        "9999999999",
        "Football Turf",
        1200
    )

    assert booking["name"] == "Test User"
    assert booking["amount"] == 1200

    taken = get_taken_slots(1, "30-09-2026")
    assert "06:00-07:00" in taken

    removed = cancel_booking_by_id(booking["id"])
    assert removed is not None

    bookings.clear()

test_booking()
print("All basic tests passed.")
