from .agent import LLMAgent
import httpx
from ..config import provider as config_provider
from ..logger import get_logger


class OpenAIAgent(LLMAgent):
    MODEL = "openai/gpt-3.5-turbo"

    def chat(self, prompt: str) -> str:
        config = config_provider()
        logger = get_logger(__name__)

        data = {
            "model": OpenAIAgent.MODEL,
            "temperature": 0.7,
            "messages": [
                {
                    "role": "system",
                    "content": "You are an AI assistant designed to revise and refine markdown articles according to given instructions."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        try:
            res = httpx.post(
                config.openrouter_url,
                json=data,
                timeout=60,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {config.openrouter_api_key}"
                }
            )
            res.raise_for_status()
            res_body = res.json()

            # return res.json()["choices"][0]["message"]["content"]
            return res_body.get("choices", [{}])[0].get("message", {}).get("content", "")

        except httpx.RequestError as e:
            logger.error(
                f"Request error occurred while connecting to OpenRouter: {e}")
        except httpx.HTTPStatusError as e:
            logger.error(
                f"HTTP error response {e.response.status_code} from OpenRouter: {e}")
        except Exception as e:
            logger.exception(f"Unexpected error occurred: {e}")

        return ""
