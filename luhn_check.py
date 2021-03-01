# Separate digits
# Read right from left - odd and even digits
# If odd, add numbers
# If even - multiple by 2, if bigger than 10, sum both digits
# Add odd and even
# If sum % 10 == 10 -> Number valid
def get_numbers(n):
    return [int(d) for d in str(n)]


def luhn_check(card_number):
    digits = get_numbers(card_number)

    even_digits = digits[-2::-2]
    odd_digits = digits[-1::-2]

    checksum = 0
    checksum = checksum + sum(odd_digits)

    for x in even_digits:
        checksum = checksum + sum(get_numbers(x * 2))
    # return checksum % 10

    if checksum % 10 == 0:
        return True
