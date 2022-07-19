"""Model for aircraft flights"""
import sys
from airtravel.aircraft import Aircraft


class Flight:
    """A flight with a particular passenger aircraft"""

    def __init__(self, flight_no: any, aircraft: Aircraft):
        try:
            if not flight_no[:2].isalpha():
                raise ValueError(f'no airline code in {flight_no}')
            if not flight_no[:2].isupper():
                raise ValueError(f'invalid airline code {flight_no}')
            if not (flight_no[2:].isdigit() and int(flight_no[2:]) <= 9999):
                raise ValueError(f'invalid route number {flight_no}')

            self._flight_number = flight_no
            self._aircraft = aircraft

            # seats allocation, row indices is one-based, but list is zero-based
            # we need to waste the one beginning entry of the list + entry in each row in rows

            rows, seats = self._aircraft.seating_plan()
            self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

            # '_' is using in the comprehension as we are not interested in the row number
            # we will use list indices instead
            # '{ letter: None for letter in seats }' is also a dictionary comprehension
            # this will create a dictionary with each key has 'None' value to show empty seat
            # we use dictionary objects as list elements as we wanted distinct element for each row

        except ValueError as e:
            print(f'invalid input: {e}', file=sys.stderr)

    # instance method must accept the reference of the actual instance when method is called (self)
    # as the first argument. 'self' is only a convention
    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._flight_number

    def airline(self):
        return self._flight_number[:2]

    def allocate_seats(self, seat, passenger):
        """Allocate a seat to passenger,

        Args:
            seat: a seat designator such as '12C' or '21F
            passenger: passenger name

        Raises:
            ValueError: If the seat is unavailable

        """

        try:
            seat_info = self._parse_seat(seat)
            if seat_info is not None:
                row, letter = self._parse_seat(seat)
            else:
                raise ValueError(f'invalid seat entry')

            if self._seating[row][letter] is not None:
                raise ValueError(f'seat {seat} already occupied')

            self._seating[row][letter] = passenger

        except (ValueError, TypeError) as e:
            print(f'invalid input: {e}', file=sys.stderr)

    def _parse_seat(self, seat):

        rows, seat_letters = self._aircraft.seating_plan()
        try:
            letter = seat[-1]
            if letter not in seat_letters:
                raise ValueError(f'invalid seat letter {letter}')

            row_text = seat[:-1]

            if not str(row_text).isdigit():
                raise TypeError(f'row must be in number. your input row is "{row_text}" of "{seat}"')

            row = int(row_text)

            if row not in rows:
                raise ValueError(f'invalid row number {row}')

            return row, letter

        except (ValueError, TypeError) as e:

            print(f'invalid input: {e}', file=sys.stderr)

    def relocate_passenger(self, from_seat, to_seat):
        """relocate a passenger to a different seat.

        Args:
            from_seat: the existing seat designated previously
            to_seat: new seat designation

        """
        try:

            from_seat_info = self._parse_seat(from_seat)
            if from_seat_info is not None:
                from_row, from_letter = from_seat_info
            else:
                raise ValueError(f'existing seat is not valid')

            if self._seating[from_row][from_letter] is None:
                raise ValueError(f'no seating exist for this seat: {from_seat}')

            to_seat_info = self._parse_seat(to_seat)
            if to_seat_info is not None:
                to_row, to_letter = to_seat_info
            else:
                raise ValueError(f'new seat designation is not valid')

            if self._seating[to_row][to_letter] is not None:
                raise ValueError(f'seat {to_seat} is already occupied')

            # relocate values
            self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
            self._seating[from_row][from_letter] = None

        except (ValueError, TypeError) as e:
            print(f'invalid input: {e}', file=sys.stderr)

    def seating_list(self):
        return self._seating

    def seat_available(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)
