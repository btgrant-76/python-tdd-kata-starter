import pytest

from src.string_calculator import calculate_string

""" Starter unit test file for the String Calculator kata.

This unit tests below support the first step of the kata and is designed to get you started practicing the 
"Three Rules". One at a time, remove the @pytest.mark.skip annotation and run pytest; the test should fail. Update the 
calculate_string implementation so the test passes. Continue in this fashion until all three tests are passing.

Once completing these, three tests, write your own tests to complete the String Calculator kata. 
"""


@pytest.mark.skip
def test_an_empty_string_yields_zero():
    assert 0 == calculate_string('')


@pytest.mark.skip
def test_a_single_number_yields_that_value():
    assert 5 == calculate_string('5')


@pytest.mark.skip
def test_two_numbers_comma_delimited_yield_the_sum():
    assert 14 == calculate_string('5,9')
