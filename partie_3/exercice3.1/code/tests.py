import pytest
from ai_corrected_version import calculate_average_robust

def test_standard_list_of_integers():
    """Test with a simple list of positive integers."""
    assert calculate_average_robust([1, 2, 3, 4, 5]) == 3.0

def test_list_with_floats():
    """Test with a list containing floating-point numbers."""
    # Use pytest.approx for comparing floats to handle precision issues
    assert calculate_average_robust([1.5, 2.5, 3.5]) == pytest.approx(2.5)

def test_list_with_negative_numbers():
    """Test with a list containing positive, negative, and zero."""
    assert calculate_average_robust([-10, 0, 10, 20]) == 5.0

def test_empty_list():
    """Test that an empty list correctly returns 0."""
    assert calculate_average_robust([]) == 0.0

def test_mixed_type_list():
    """Test the primary robustness case: a list with mixed types."""
    # The function should ignore 'three', None, and the empty list []
    data = [1, 2, 'three', 4, None, 5.0, []]
    # It should calculate the average of 1, 2, 4, and 5.0
    expected_average = (1 + 2 + 4 + 5.0) / 4
    assert calculate_average_robust(data) == pytest.approx(expected_average)

def test_list_with_only_non_numeric_values():
    """Test that a list with no numbers correctly returns 0."""
    assert calculate_average_robust(['apple', 'banana', None]) == 0.0