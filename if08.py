def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    two_digit = 9<a<100
    three_digit = 99<a<1000
    finish = 0

    if two_digit and a%2!=0:
        finish = 'two-digit odd number'
    elif two_digit and a%2==0:
        finish = 'two-digit even number'
    elif three_digit and a%2!=0:
        finish = 'three-digit odd number'
    elif three_digit and a%2==0:
        finish = 'three-digit even number'
    return finish
print(main(30))