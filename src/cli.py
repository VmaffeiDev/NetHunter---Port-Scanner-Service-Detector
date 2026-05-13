"""CLI for NetHunter port scanner."""

from __future__ import annotations

import argparse
from typing import List

from src.detector import detect_service
from src.scanner import scan_ports


MIN_PORT = 1
MAX_PORT = 65535


def _validate_port(port: int) -> None:
    if port < MIN_PORT or port > MAX_PORT:
        raise ValueError(f"Porta inválida: {port}. Use valores entre {MIN_PORT} e {MAX_PORT}.")


def parse_ports(raw_ports: str) -> List[int]:
    """Parse comma-separated ports and ranges into a sorted unique list."""

    ports: List[int] = []
    for chunk in raw_ports.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue

        if "-" in chunk:
            start_raw, end_raw = chunk.split("-", maxsplit=1)
            start, end = int(start_raw), int(end_raw)
            if start > end:
                raise ValueError(f"Intervalo inválido: {chunk}. Use início <= fim.")
            for port in range(start, end + 1):
                _validate_port(port)
                ports.append(port)
        else:
            port = int(chunk)
            _validate_port(port)
            ports.append(port)

    if not ports:
        raise ValueError("Nenhuma porta válida foi informada.")

    return sorted(set(ports))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="nethunter-scan",
        description="Scanner simples de portas e detector de serviço provável.",
    )
    parser.add_argument("host", help="Host alvo (ex.: 127.0.0.1)")
    parser.add_argument(
        "--ports",
        default="22,80,443,8080",
        help="Lista de portas ou intervalo. Ex.: 22,80,443 ou 1-1024",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=0.5,
        help="Timeout da conexão por porta, em segundos (padrão: 0.5)",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.timeout <= 0:
        parser.error("--timeout deve ser maior que zero.")

    try:
        ports = parse_ports(args.ports)
    except ValueError as exc:
        parser.error(str(exc))

    results = scan_ports(host=args.host, ports=ports, timeout=args.timeout)

    print(f"Escaneando {args.host}...")
    for result in results:
        status = "OPEN" if result.is_open else "CLOSED"
        service = detect_service(result.port)
        print(f"{result.port:<5} {status:<6} {service}")


if __name__ == "__main__":
    main()
