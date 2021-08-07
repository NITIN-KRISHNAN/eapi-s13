import parking
import types
import datetime


def test_if_generator():
    assert isinstance(parking.read_file_gen(), types.GeneratorType)


def test_if_length_matches():
    length = 0
    for _ in parking.read_file_gen():
        length += 1
    assert length == 1000


def test_make_violation_count():
    assert parking.find_violations_by_make("BMW") == 34


def test_if_namedtuple():
    gen = parking.read_file_gen()
    ticket = next(gen)
    assert isinstance(ticket, parking.Ticket)
    assert isinstance(ticket.issue_date, datetime.date)
    assert isinstance(ticket.summon_num, int)
    assert isinstance(ticket.violation_code, int)
