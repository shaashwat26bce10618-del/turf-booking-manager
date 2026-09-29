# Turf Booking Manager

## Overview

Turf Booking Manager is a simple Python console application for managing sports turf bookings.

A user can check available slots, make a booking, search for bookings, cancel bookings and view simple booking statistics.

## Features

- Check turf availability
- Book a turf slot
- View all bookings
- Search bookings
- Cancel bookings
- View latest bookings
- View a booking summary
- Basic input validation
- Basic testing

## Technologies Used

- Python
- Python lists and dictionaries
- Functions
- Loops and conditions
- datetime module
- random module

## Project Structure

```text
turf_booking_manager/
|
|-- src/
|   |-- main.py
|   |-- data.py
|   |-- validation.py
|   |-- booking.py
|   |-- display.py
|   |-- reports.py
|
|-- tests/
|   |-- test_project.py
|
|-- docs/
|   |-- architecture.png
|   |-- workflow.png
|   |-- use_case.png
|   |-- class_diagram.png
|   |-- sequence_diagram.png
|
|-- README.md
|-- statement.md
|-- requirements.txt
|-- project_report.pdf
```

## How to Run

Open a terminal inside the `src` folder and run:

```text
python main.py
```

No external Python packages are required for the actual application.

## Testing

From the `tests` folder, run:

```text
python test_project.py
```

The test checks booking creation, checking an occupied slot and cancellation.

## Data Storage

The current version stores bookings in memory using a Python list. This means bookings are removed when the program is closed.

A future version could use a database or file for permanent storage.
