# mini-ai-agent

A minimal Python scaffold for building and testing small AI agents.

## Quick start

```bash
python3 -m mini_ai_agent.cli "hello"
```

Or install the local package entrypoint:

```bash
pip install -e .
mini-ai-agent "hello"
```

## Interactive mode

```bash
python3 -m mini_ai_agent.cli
```

Commands:

- `history` prints the current in-memory transcript.
- `exit` or `quit` leaves the session.

## HTTP server

Start the server on port `9090`:

```bash
python3 -m mini_ai_agent.server
```

Or if installed locally:

```bash
mini-ai-agent-server
```

Send a message:

```bash
curl -X POST http://127.0.0.1:9090/message \
  -H "Content-Type: application/json" \
  -d '{"message":"hello"}'
```

Response:

```json
{"message": "HELLO"}
```

Open `http://127.0.0.1:9090/` in a browser for an interactive test page backed by the same endpoint.

## Development

```bash
pytest
```
