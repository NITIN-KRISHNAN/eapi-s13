from collections import namedtuple
import csv
import datetime

FILE_NAME = "nyc_parking_tickets_extract-1.csv"
Ticket = namedtuple("Ticket", "summon_num, plate_id, reg_state, plate_type, issue_date, violation_code,"
                              "vehicle_body_type, vehicle_make, violation_desc")


def read_file_gen():
    """
    Generator to read the parking tickets csv file, where each ticket row is returned as a Ticket NamedTuple
    :return: Generator to read the parking tickets csv file
    """
    with open(FILE_NAME) as parking_tickets_csv:
        csv_reader = csv.reader(parking_tickets_csv, delimiter=',')
        line_num = 0
        for line in csv_reader:
            # skip first row as it contains headers
            if line_num == 0:
                line_num += 1
            else:
                yield form_ticket(line)


def form_ticket(line: list) -> Ticket:
    """
    Function to convert list of values from csv to Ticket namedtuple
    :param line: the list of values for each row of the parking tickets csv
    :return: Ticket named tuple
    """
    summon_num = int(line[0])
    plate_id = line[1]
    reg_state = line[2]
    plate_type = line[3]
    issue_date = datetime.datetime.strptime(line[4], "%m/%d/%Y").date()
    violation_code = int(line[5])
    vehicle_body_type = line[6]
    vehicle_make = line[7]
    violation_desc = line[8]
    ticket = Ticket(summon_num, plate_id, reg_state, plate_type, issue_date,violation_code, vehicle_body_type,
                  vehicle_make,violation_desc)
    # print(ticket)
    return ticket


def find_violations_by_make_all():
    """
    Function to find the number of violations for each vehicle make
    :return: dict of make_violations_count
    """
    make_violations_count = dict()
    tickets_gen = read_file_gen()
    for ticket in tickets_gen:
        make = ticket.vehicle_make
        violation_count = make_violations_count.get(make, 0)
        violation_count += 1
        make_violations_count[make] = violation_count
    print(make_violations_count)
    return make_violations_count


def find_violations_by_make(make: str) -> int:
    """
    Function to find the number of violations for given vehicle make, this function reuses find_violations_by_make_all
    :param make: vehicle make whose number of violations are to be found out
    :return: number of violations for the given vehicle make
    """
    make_violations_count = find_violations_by_make_all()
    print(make, make_violations_count.get(make, 0))
    return make_violations_count.get(make, 0)


def find_violations_by_make_1(make_input: str) -> int:
    """
    Function to find the number of violations for given vehicle make, this function calculates the violations count
    independently by iterating through the generator
    :param make_input: vehicle make whose number of violations are to be found out
    :return: number of violations for the given vehicle make
    """
    make_violations_count = dict()
    tickets_gen = read_file_gen()
    for ticket in tickets_gen:
        make = ticket.vehicle_make
        if make == make_input:
            violation_count = make_violations_count.get(make, 0)
            violation_count += 1
            make_violations_count[make] = violation_count
    return make_violations_count.get(make_input, 0)
