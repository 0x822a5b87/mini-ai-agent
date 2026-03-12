from __future__ import annotations

import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


HOST = "0.0.0.0"
PORT = 9090
STATIC_DIR = Path(__file__).with_name("static")
INDEX_FILE = STATIC_DIR / "index.html"


def uppercase_message(message: str) -> str:
    return message.upper()


class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:  # noqa: N802
        if self.path != "/message":
            self.send_error(HTTPStatus.NOT_FOUND, "Not Found")
            return

        content_length = self.headers.get("Content-Length")
        if content_length is None:
            self._send_json(HTTPStatus.BAD_REQUEST, {"error": "Missing Content-Length header"})
            return

        try:
            raw_body = self.rfile.read(int(content_length))
            payload = json.loads(raw_body)
        except (ValueError, json.JSONDecodeError):
            self._send_json(HTTPStatus.BAD_REQUEST, {"error": "Request body must be valid JSON"})
            return

        message = payload.get("message")
        if not isinstance(message, str):
            self._send_json(HTTPStatus.BAD_REQUEST, {"error": "'message' must be a string"})
            return

        self._send_json(HTTPStatus.OK, {"message": uppercase_message(message)})

    def do_GET(self) -> None:  # noqa: N802
        if self.path in {"/", "/index.html"}:
            self._send_file(INDEX_FILE, "text/html; charset=utf-8")
            return

        self.send_error(HTTPStatus.NOT_FOUND, "Not Found")

    def log_message(self, format: str, *args: object) -> None:
        return

    def _send_json(self, status: HTTPStatus, payload: dict[str, str]) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path: Path, content_type: str) -> None:
        if not path.exists():
            self.send_error(HTTPStatus.NOT_FOUND, "Not Found")
            return

        body = path.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def run_server(host: str = HOST, port: int = PORT) -> None:
    server = ThreadingHTTPServer((host, port), MessageHandler)
    print(f"Listening on http://{host}:{port}")
    server.serve_forever()


def main() -> int:
    run_server()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
