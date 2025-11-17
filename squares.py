"""Computation of weighted average of squares."""
import argparse
import sys # Import sys to use exit()

def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    8.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    
    sum_of_weighted_squares = sum(
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    )
    
    sum_of_weights = sum(effective_weights)
    
    if sum_of_weights == 0:
        raise ValueError("Sum of weights cannot be zero.")

    return sum_of_weighted_squares / sum_of_weights

def read_data_from_file(filename):
    """
    Reads a file with one number per line.
    Returns a list of floats.
    """
    data_list = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                # .strip() removes whitespace/newlines
                # if line.strip() ensures we skip empty lines
                if line.strip():
                    data_list.append(float(line.strip()))
    except FileNotFoundError:
        print(f"Error: File not found at {filename}")
        sys.exit(1)
    except ValueError:
        print(f"Error: Non-numeric value found in {filename}")
        sys.exit(1)
    
    if not data_list:
        print(f"Error: No data found in file {filename}")
        sys.exit(1)
        
    return data_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Calculate the average of squares of numbers from files.'
    )

    parser.add_argument(
        'numbers_file', 
        metavar='<file_numbers>',
        help='The path to a file containing numbers (one per line).'
        )
    
    parser.add_argument(
        '--weights', 
        metavar='<file_weights>',
        required=False,
        help='The path to an optional file containing weights (one per line).'
        )

    args = parser.parse_args()

    numbers_list = read_data_from_file(args.numbers_file)

    weights_list = None
    if args.weights: # args.weights is the filename (a string)
        weights_list = read_data_from_file(args.weights)


        

    if weights_list:
        print(f"Numbers read from file: {numbers_list}")
        print(f"Weights read from file: {weights_list}")
    else:
        print(f"Numbers read from file: {numbers_list}")
        print("No weights file provided, using constant weights.")

    try:
        # Pass the correct lists to the function
        result = average_of_squares(numbers_list, weights_list)
        print(f"Average of squares: {result}")
    except (ValueError, AssertionError) as e:
        # Catch errors from average_of_squares (e.g., mismatched lengths)
        print(f"Error during calculation: {e}")
        sys.exit(1)