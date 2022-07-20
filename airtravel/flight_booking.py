import sys
from pprint import pprint as pp
from airtravel.flight import Flight
from airtravel.aircraft import Aircraft
from airtravel.cardprinters import console_card_printer


def book_flight():
    f = Flight('BA758', Aircraft('G-EUPT', 'Airbus A777', seat_rows=22, num_seats_per_row=6))
    f.allocate_seats('12A', 'Roger Federer')
    f.allocate_seats('15F', 'Novak Djokovic')
    f.allocate_seats('15E', 'Rafael Nadal')
    f.allocate_seats('2C', 'Marian Cilic')
    f.allocate_seats('2D', 'Botic V')
    f.allocate_seats('2E', 'Alexander Zverez')
    f.allocate_seats('2F', 'Dominic Thiem')
    f.allocate_seats('12B', 'Himura Kenshin')
    return f


def display_seats(f: Flight):
    pp(f.seating_list())


def relocate_seat(f: Flight, from_seat: str, to_seat: str):
    f.relocate_passenger(from_seat, to_seat)


def seat_available(f: Flight):
    return f.seat_available()


def make_boarding_cards(f: Flight, cp: console_card_printer):
    for passenger, seat in sorted(f.passenger_seats()):
        cp.console_card_printer(passenger, seat, f.number(), f.aircraft_model())
