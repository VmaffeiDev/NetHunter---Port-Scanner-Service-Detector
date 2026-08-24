"""Port scanning utilities."""

from __future__ import annotations

import socket
from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class PortResult:
    """Represents the status of a scanned port."""

    port: int
    is_open: bool


def _is_port_open(host: str, port: int, timeout: float = 0.5) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex((host, port)) == 0


def scan_ports(host: str, ports: Iterable[int], timeout: float = 0.5) -> List[PortResult]:
    """Scan a host and return open/closed status for each port in order."""

    results: List[PortResult] = []
    for port in ports:
        if port < 1 or port > 65535:
            raise ValueError(f"Porta inválida: {port}. Use valores entre 1 e 65535.")

        results.append(PortResult(port=port, is_open=_is_port_open(host, port, timeout)))

    return results
