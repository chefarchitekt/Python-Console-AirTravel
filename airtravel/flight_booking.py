import sys
from pprint import pprint as pp
from airtravel.flight import Flight
from airtravel.aircraft import (Aircraft, registered_aircrafts)


def get_registered_aircrafts():
    return registered_aircrafts()


def book_flight():
    aircrafts = registered_aircrafts()
    try:
        registered_aircraft = aircrafts['A758-2009-002']
        if registered_aircraft is not None:
            reg_no, model, rows, num_seats = registered_aircraft
        else:
            raise ValueError(f'aircraft is not registered, booking not possible for "A758-2009-002"')

        f = Flight('BA758', Aircraft(reg_no, model, rows, num_seats))
        f.allocate_seats('12A', 'Roger Federer')
        f.allocate_seats('15F', 'Novak Djokovic')
        f.allocate_seats('15E', 'Rafael Nadal')
        f.allocate_seats('2C', 'Marian Cilic')
        f.allocate_seats('2D', 'Botic V')
        f.allocate_seats('2E', 'Alexander Zverez')
        f.allocate_seats('2F', 'Dominic Thiem')
        f.allocate_seats('12B', 'Himura Kenshin')
        return f
    except ValueError as e:
        print(f'booking error; {e}', file=sys.stderr)


def display_seats(f: Flight):
    pp(f.seating_list())


def relocate_seat(f: Flight, from_seat: str, to_seat: str):
    f.relocate_passenger(from_seat, to_seat)


def seat_available(f: Flight):
    return f.seat_available()


def make_boarding_cards(f: Flight, cp):
    for passenger, seat in sorted(f.passenger_seats()):
        cp(passenger, seat, f.number(), f.aircraft_model())
