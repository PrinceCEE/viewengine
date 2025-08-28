class Config:
    """Config holds runtime configurations sourced from environment variables or an available env file."""

    def __init__(self) -> None:
        pass

__instance__ = Config()

def provider() -> Config:
    return __instance__