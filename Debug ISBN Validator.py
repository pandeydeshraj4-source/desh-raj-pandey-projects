def validate_isbn(isbn, length):
    isbn = isbn.strip()

    if length not in (10, 13):
        print('Length should be 10 or 13.')
        return

    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    try:
        main_digits = isbn[:-1]
        given_check_digit = isbn[-1].upper()
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print("Invalid character was found.")
        return

    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    elif length == 13:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    if given_check_digit == str(expected_check_digit):
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for i, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - i)
    check_digit = (11 - (digits_sum % 11)) % 11
    return 'X' if check_digit == 10 else str(check_digit)


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for i, digit in enumerate(main_digits_list):
        if i % 2 == 0:
            digits_sum += digit
        else:
            digits_sum += digit * 3
    check_digit = (10 - (digits_sum % 10)) % 10
    return str(check_digit)


def main():
    user_input = input('Enter ISBN and length: ')
    try:
        isbn, length_str = user_input.split(',')
    except (ValueError, IndexError):
        print('Enter comma-separated values.')
        return

    try:
        length = int(length_str)
    except ValueError:
        print('Length must be a number.')
        return

    validate_isbn(isbn, length)

main()

#HOW THIS LOGIC WORKS
# Input
#  ↓
# Clean the input
#  ↓
# Check length
#  ↓
# Separate main digits and check digit
#  ↓
# Convert characters to integers
#  ↓
# Apply ISBN-10 or ISBN-13 formula
#  ↓
# Compare expected vs given check digit
#  ↓
# Print result