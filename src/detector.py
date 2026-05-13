"""Service detection for open ports."""

from __future__ import annotations

from typing import Dict

COMMON_PORT_SERVICES: Dict[int, str] = {
    21: "ftp",
    22: "ssh",
    25: "smtp",
    53: "dns",
    80: "http",
    110: "pop3",
    143: "imap",
    443: "https",
    3306: "mysql",
    5432: "postgresql",
    6379: "redis",
    8080: "http-alt",
}


def detect_service(port: int) -> str:
    """Infer probable service name from the port number."""

    return COMMON_PORT_SERVICES.get(port, "unknown")
