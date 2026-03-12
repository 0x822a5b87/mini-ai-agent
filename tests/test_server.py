from mini_ai_agent.server import uppercase_message


def test_uppercase_message() -> None:
    assert uppercase_message("hello, world") == "HELLO, WORLD"
