import pytest

from src.string_calculator import calculate_string


# TODO:  change from returns to yields?
# TODO:  write up some instructions for this file specifically using https://realpython.com/documenting-python-code/



@pytest.mark.skip
def test_an_empty_string_returns_zero():
    assert 0 == calculate_string('')


@pytest.mark.skip
def test_a_single_number_returns_that_value():
    assert 5 == calculate_string('5')


@pytest.mark.skip
def test_two_numbers_comma_delimited_return_the_sum():
    assert 14 == calculate_string('5,9')


@pytest.mark.skip
def test_two_numbers_newline_delimited_returns_the_sum():
    assert 14 == calculate_string('5\n9')


@pytest.mark.skip  # TODO change this to a parameterized test
def test_three_numbers_delimited_either_way_returns_the_sum():
    assert 23 == calculate_string('5\n9\n9')
    assert 23 == calculate_string('5,9,9')

# def test_negative_numbers_raise_an_exception():

#
# @Disabled
# @Test
# void negativeNumbersThrowAnException() {
#     Stream.of('-1', '5,-1,9')
#         .forEach(numString -> {
# try {
# testMe.calculateString(numString);
# fail("an exception should have been thrown for " + numString);
# } catch (IllegalArgumentException e) {
# assertEquals("negative numbers aren't allowed:  -1", e.getMessage());
# }
# });
# }
#
# @Disabled
#  @Test
# void numbersGreaterThan1000AreIgnored() {
#     assertEquals(23, testMe.calculateString('5,9,1025,9'));
# }
#
# @Disabled
#  @Test
# void aSingleCharDelimiterCanBeDefinedOnTheFirstLine() {
#     assertEquals(23, testMe.calculateString('#\n5#9#9'));
# }
#
# @Disabled
#  @Test
# void aMultiCharDelimiterCanBeDefinedOnTheFirstLine() {
#     assertEquals(23, testMe.calculateString('[###]\n5###9###9'));
# }
#
# @Disabled
#  @Test
# void manySingleOrMultiCharDelimitersCanBeDefined() {
#     assertEquals(23, testMe.calculateString('[|||][$$]\n5|||9$$9'));
# }
