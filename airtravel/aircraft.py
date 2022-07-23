"""Aircraft Class"""
import sys


# aircraft seating plan, letter 'I' is omitted to avoid confusion with number 1
class Aircraft:
    def __init__(self, registration, model, seat_rows, num_seats_per_row):
        try:

            self._registration = registration
            self._model = model
            self._seat_rows = seat_rows
            self._num_seats_per_row = num_seats_per_row

        except ValueError as e:
            print(f'invalid input arguments: {e}', file=sys.stderr)

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return range(1, self._seat_rows + 1), "ABCDEFGHJKLMNOPQRS"[:self._num_seats_per_row]


_registered_aircrafts = {}


def register_an_aircraft(register_no, model, seat_rows, num_seats_per_row):
    key = register_no
    value = tuple([register_no, model, seat_rows, num_seats_per_row])
    entry = {key: value}
    _registered_aircrafts.update(entry)


def registered_aircrafts():
    register_an_aircraft('A777-2009-001', 'Airbus A777', seat_rows=43, num_seats_per_row=12)
    register_an_aircraft('A758-2009-002', 'Airbus A758', seat_rows=22, num_seats_per_row=6)
    return _registered_aircrafts
