def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    d=0
    if a>0:
        d+=1
    if b>0:
        d+=1
    if c>0:
        d+=1

    if d>1:
        return 'There are a lot of positive numbers'
    else:
        return 'There are a lot of negative numbers'
        
    return d