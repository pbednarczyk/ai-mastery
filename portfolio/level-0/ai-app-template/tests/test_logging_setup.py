import json
import logging
import sys

from app.logging_setup import JsonFormatter, setup_logging


def test_setup_logging_sets_handler_and_level() -> None:
    root = logging.getLogger()
    original_level = root.level
    original_handlers = root.handlers[:]

    try:
        setup_logging("warning")

        assert root.level == logging.WARNING
        assert len(root.handlers) == 1
        handler = root.handlers[0]
        assert isinstance(handler, logging.StreamHandler)
        assert handler.stream is sys.stdout
    finally:
        root.handlers.clear()
        root.handlers.extend(original_handlers)
        root.setLevel(original_level)


def test_json_formatter_returns_json_string() -> None:
    formatter = JsonFormatter()
    record = logging.getLogger("app").makeRecord(
        name="app",
        level=logging.INFO,
        fn=__file__,
        lno=10,
        msg="message",
        args=(),
        exc_info=None,
    )

    payload = json.loads(formatter.format(record))

    assert payload["level"] == "INFO"
    assert payload["logger"] == "app"
    assert payload["message"] == "message"
    assert "ts" in payload
    assert "request_id" in payload


def test_json_formatter_includes_exception_info() -> None:
    formatter = JsonFormatter()

    try:
        raise ValueError("boom")
    except ValueError:
        exc = sys.exc_info()

    record = logging.getLogger("app").makeRecord(
        name="app",
        level=logging.ERROR,
        fn=__file__,
        lno=42,
        msg="error",
        args=(),
        exc_info=exc,
    )

    payload = json.loads(formatter.format(record))

    assert payload["level"] == "ERROR"
    assert "ValueError: boom" in payload["exc_info"]
