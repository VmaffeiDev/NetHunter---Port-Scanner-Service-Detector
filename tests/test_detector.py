from src.detector import detect_service


def test_detect_service_known_port():
    assert detect_service(80) == "http"


def test_detect_service_unknown_port():
    assert detect_service(9999) == "unknown"
