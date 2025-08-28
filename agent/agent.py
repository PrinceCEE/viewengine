from abc import ABC, abstractmethod

class LLMAgent(ABC):
    """The Agent interface which should be implemented by the agent clients"""

    @abstractmethod
    def chat(self, prompt: str)-> str:
        """Takes a prompt and returns a response from the LLM"""
        pass