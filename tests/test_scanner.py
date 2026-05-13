import socket

from src.scanner import scan_ports


def test_scan_ports_detects_open_and_closed_ports():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 0))
    server.listen(1)

    open_port = server.getsockname()[1]
    closed_port = open_port + 1

    try:
        results = scan_ports("127.0.0.1", [open_port, closed_port], timeout=0.2)
    finally:
        server.close()

    result_map = {item.port: item.is_open for item in results}
    assert result_map[open_port] is True
    assert result_map[closed_port] is False


def test_scan_ports_invalid_port_raises():
    try:
        scan_ports("127.0.0.1", [0])
    except ValueError as exc:
        assert "Porta inválida" in str(exc)
    else:
        raise AssertionError("Era esperado ValueError para porta inválida")
