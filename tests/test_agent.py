from mini_ai_agent import MiniAgent


def test_reply_echoes_message_with_name() -> None:
    agent = MiniAgent(name="agent")
    assert agent.reply("hello") == "agent> hello"


def test_history_command_without_prior_messages() -> None:
    agent = MiniAgent()
    assert agent.reply("history") == "No history yet."
