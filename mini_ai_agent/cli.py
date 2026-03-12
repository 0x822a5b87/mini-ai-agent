from __future__ import annotations

import argparse

from .agent import build_default_agent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the mini AI agent.")
    parser.add_argument(
        "prompt",
        nargs="*",
        help="Optional one-shot prompt. Omit to start an interactive session.",
    )
    parser.add_argument(
        "--name",
        default="mini",
        help="Agent name used in replies.",
    )
    return parser


def run_interactive(name: str) -> int:
    agent = build_default_agent()
    agent.name = name
    print("mini-ai-agent interactive mode. Type 'exit' to quit.")

    while True:
        try:
            user_input = input("> ")
        except EOFError:
            print()
            return 0

        if user_input.strip().lower() in {"exit", "quit"}:
            return 0

        print(agent.reply(user_input))


def main() -> int:
    args = build_parser().parse_args()
    prompt = " ".join(args.prompt).strip()

    if prompt:
        agent = build_default_agent()
        agent.name = args.name
        print(agent.reply(prompt))
        return 0

    return run_interactive(args.name)


if __name__ == "__main__":
    raise SystemExit(main())
