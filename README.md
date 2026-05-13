# NetHunter — Port Scanner & Service Detector

Ferramenta em Python para **varredura de portas TCP** e **detecção simples de serviço provável por porta**.

## Recursos implementados
- varredura de portas TCP com timeout configurável;
- classificação de status por porta (`OPEN` / `CLOSED`);
- detecção básica de serviço por portas comuns (HTTP, HTTPS, SSH, etc.);
- CLI para uso rápido em terminal;
- testes automatizados para scanner, detector e parser de portas.

> ⚠️ Use apenas em ambientes autorizados (infra própria/lab ou com permissão explícita).

## Estrutura do projeto
```text
.
├── README.md
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── detector.py
│   └── scanner.py
└── tests/
    ├── test_cli.py
    ├── test_detector.py
    └── test_scanner.py
```

## Como executar
### 1) Rodar scanner via CLI
```bash
python -m src.cli 127.0.0.1 --ports 22,80,443,8080
```

Exemplo com intervalo:
```bash
python -m src.cli 127.0.0.1 --ports 1-1024 --timeout 0.2
```

### 2) Rodar testes
```bash
pytest -q
```

## Próximas melhorias sugeridas
- detecção por banner grab (além de portas conhecidas);
- suporte a UDP;
- execução concorrente para scans maiores;
- exportação de resultado (JSON/CSV);
- CI com lint e testes.
