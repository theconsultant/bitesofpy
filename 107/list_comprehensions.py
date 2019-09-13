def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    number_list = [number for number in numbers if number > 0 if number % 2 == 0]
    return(number_list)