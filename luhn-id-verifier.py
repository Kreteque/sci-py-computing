def verify_card_number(card_number):
    total_sum = 0
    # Iterate through the card number, starting from the last digit
    for i, digit in enumerate(reversed(card_number)):
        digit = int(digit)
        # If the index is odd (1-based index), it's an "even" position for Luhn algorithm
        if i % 2 == 1:
            # Double the digit and sum the digits of the result if >= 10
            doubled = digit * 2
            if doubled >= 10:
                total_sum += (doubled // 10) + (doubled % 10)
            else:
                total_sum += doubled
        else:
            # Odd positions (1-based index) are added as is
            total_sum += digit

    return total_sum % 10 == 0

def main():
    print("Cek validasi nomor kartu kredit atau debit")
    card_number = input('Masukan nomor kartu kredit atau debit: ')
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()
