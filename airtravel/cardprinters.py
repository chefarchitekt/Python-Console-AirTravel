def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f'| Name: {passenger}' \
             f'  Flight: {flight_number}' \
             f'  Seat: {seat}' \
             f'  Aircraft: {aircraft}' \
             ' |'
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()  # blank line

def html_card_printer():
    pass
