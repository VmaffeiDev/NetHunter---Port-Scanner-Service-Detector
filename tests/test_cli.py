from src.cli import parse_ports


def test_parse_ports_list_and_range():
    assert parse_ports("22,80,100-102") == [22, 80, 100, 101, 102]


def test_parse_ports_removes_duplicates():
    assert parse_ports("80,80,79-81") == [79, 80, 81]
