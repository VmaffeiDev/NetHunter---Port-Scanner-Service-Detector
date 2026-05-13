"""CLI for NetHunter port scanner."""

from __future__ import annotations

import argparse
from typing import List

from src.detector import detect_service
from src.scanner import scan_ports


def parse_ports(raw_ports: str) -> List[int]:
    ports: List[int] = []
    for chunk in raw_ports.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue

        if "-" in chunk:
            start, end = chunk.split("-", maxsplit=1)
            ports.extend(range(int(start), int(end) + 1))
        else:
            ports.append(int(chunk))

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

    ports = parse_ports(args.ports)
    results = scan_ports(host=args.host, ports=ports, timeout=args.timeout)

    print(f"Escaneando {args.host}...")
    for result in results:
        status = "OPEN" if result.is_open else "CLOSED"
        service = detect_service(result.port)
        print(f"{result.port:<5} {status:<6} {service}")


if __name__ == "__main__":
    main()
