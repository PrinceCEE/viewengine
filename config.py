from dotenv import load_dotenv
import os


class Config:
    """Config holds runtime configurations sourced from environment variables or an available env file."""

    def __init__(self) -> None:
        load_dotenv()

        self.openrouter_api_key = os.getenv("OPENROUTER_API_KEY", "")
        self.openrouter_url = os.getenv("OPENROUTER_URL", "")
        pass


__instance__ = Config()


def provider() -> Config:
    return __instance__
