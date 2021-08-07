# epai-s13 - Generators

##Goal 1
Create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate - i.e. if the column is a date, you should be storing dates in the named tuple, if the field is an integer, then it should be stored as an integer, etc

## Goal 2
Calculate the number of violations by car make.

###Note:
- Try to use lazy evaluation as much as possible - it may not always be possible though! That's OK, as long as it's kept to a minimum.
- No Test Cases

## Functions used
### read_file_gen
    Generator to read the parking tickets csv file, where each ticket row is returned as a Ticket NamedTuple
    :return: Generator to read the parking tickets csv file
### form_ticket
    Function to convert list of values from csv to Ticket namedtuple
    :param line: the list of values for each row of the parking tickets csv
    :return: Ticket named tuple
### find_violations_by_make_all
    Function to find the number of violations for each vehicle make
    :return: dict of make_violations_count
### find_violations_by_make
    Function to find the number of violations for given vehicle make, this function reuses find_violations_by_make_all
    :param make: vehicle make whose number of violations are to be found out
    :return: number of violations for the given vehicle make
### find_violations_by_make_1
    Function to find the number of violations for given vehicle make, this function calculates the violations count
    independently by iterating through the generator
    :param make_input: vehicle make whose number of violations are to be found out
    :return: number of violations for the given vehicle make

## Test cases
```
=================================================================== test session starts ===================================================================
platform darwin -- Python 3.8.1, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/local/bin/python3.8
cachedir: .pytest_cache
rootdir: /Users/Krish/Downloads/epai/eapi-s13
plugins: Faker-4.1.3, anyio-3.2.1
collected 4 items                                                                                                                                         

test_parking.py::test_if_generator PASSED                                                                                                           [ 25%]
test_parking.py::test_if_length_matches PASSED                                                                                                      [ 50%]
test_parking.py::test_make_violation_count PASSED                                                                                                   [ 75%]
test_parking.py::test_if_namedtuple PASSED                                                                                                          [100%]

==================================================================== 4 passed in 0.23s ====================================================================
```