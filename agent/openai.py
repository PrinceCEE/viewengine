from .agent import LLMAgent

class OpenAIAgent(LLMAgent):
    def chat(self, prompt: str) -> str:
        return super().chat(prompt)