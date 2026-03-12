from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class MiniAgent:
    """A tiny rule-based agent with in-memory history."""

    name: str = "mini"
    system_prompt: str = (
        "You are a concise helper. Answer directly, ask for missing context only "
        "when required, and keep state only within this session."
    )
    history: list[tuple[str, str]] = field(default_factory=list)

    def reply(self, user_message: str) -> str:
        message = user_message.strip()
        if not message:
            response = "Provide an instruction or a question."
        elif message.lower() in {"history", "/history"}:
            if not self.history:
                response = "No history yet."
            else:
                turns = [f"{idx}. {text}" for idx, (_, text) in enumerate(self.history, start=1)]
                response = "\n".join(turns)
        else:
            response = f"{self.name}> {message}"

        self.history.append(("user", message))
        self.history.append(("assistant", response))
        return response


def build_default_agent() -> MiniAgent:
    return MiniAgent()
