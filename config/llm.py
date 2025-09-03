from langchain_openai.chat_models import ChatOpenAI
from config.env import OPENAI_API_KEY

class LlmService:
    @classmethod
    def get_model(cls, model_name: str = "gpt-4o-mini"):
        if not OPENAI_API_KEY:
            raise ValueError("Issue in OpenAI API Key!")

        try:
            llm = ChatOpenAI(model=model_name, temperature=0.5)
            return llm
        except Exception:
            return None
