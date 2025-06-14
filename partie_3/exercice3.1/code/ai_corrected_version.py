def calculate_average_robust(items_list):
    """
    Calculates the average of all numeric values in a list.

    This function iterates through a list, includes only integers and floats
    in the calculation, and safely ignores all other data types.

    Args:
        items_list (list): A list that can contain a mix of data types.

    Returns:
        float: The calculated average of the numbers in the list. 
               Returns 0.0 if the list is empty or contains no numbers.
    """
    # Create a new list containing only the numbers (integers or floats)
    numbers_only = [num for num in items_list if isinstance(num, (int, float))]

    # If there are no numbers in the list, return 0 to avoid a ZeroDivisionError
    if not numbers_only:
        return 0.0

    # Calculate the sum and average of the valid numbers
    total = sum(numbers_only)
    average = total / len(numbers_only)
    
    return average

# --- Examples of Usage ---

# Example 1: The original list that caused an error
my_mixed_list = [1, 2, 'three', 4, 5.0]
avg1 = calculate_average_robust(my_mixed_list)
print(f"Average of the mixed list: {avg1}")  # Will correctly calculate (1+2+4+5.0)/4

# Example 2: An empty list
my_empty_list = []
avg2 = calculate_average_robust(my_empty_list)
print(f"Average of the empty list: {avg2}")

# Example 3: A list with no numbers
my_non_numeric_list = ['a', 'b', None]
avg3 = calculate_average_robust(my_non_numeric_list)
print(f"Average of the non-numeric list: {avg3}")
