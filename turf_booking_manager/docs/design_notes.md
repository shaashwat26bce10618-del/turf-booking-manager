# Design Notes

## Functional Modules

1. Availability - checks which slots are free.
2. Booking - creates and cancels bookings.
3. Booking Management - searches and displays bookings.
4. Reporting - shows recent bookings and summary information.
5. Validation - checks user input.

## Non-Functional Requirements

### Usability
The program uses simple numbered menus and clear messages.

### Reliability
Invalid numbers, dates and phone numbers are checked before processing.

### Maintainability
The program is divided into small Python files and functions.

### Error Handling
Invalid input is handled using loops and basic exception handling.

## Storage

Bookings are stored in a Python list while the program is running.

## Limitations

The current program does not permanently save bookings after the program closes.

## Future Improvements

- Add database storage
- Add login for staff
- Add online payment
- Add a graphical interface
- Add booking date reports
