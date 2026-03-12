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

## Development

```bash
pytest
```
