import pytest

from src.cli import parse_ports


def test_parse_ports_list_and_range():
    assert parse_ports("22,80,100-102") == [22, 80, 100, 101, 102]


def test_parse_ports_removes_duplicates():
    assert parse_ports("80,80,79-81") == [79, 80, 81]


def test_parse_ports_rejects_descending_range():
    with pytest.raises(ValueError, match="Intervalo inválido"):
        parse_ports("100-90")


def test_parse_ports_rejects_invalid_port_number():
    with pytest.raises(ValueError, match="Porta inválida"):
        parse_ports("0,80")


def test_parse_ports_rejects_empty_input():
    with pytest.raises(ValueError, match="Nenhuma porta válida"):
        parse_ports(" , ")
