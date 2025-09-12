from langchain_openai.chat_models import ChatOpenAI
#from langchain_cerebras import ChatCerebras
from cerebras.cloud.sdk import Cerebras
from config.env import OPENAI_API_KEY, CEREBRAS_API_KEY

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

    @classmethod
    def get_model_with_cerebras_key(cls, model_name: str = "gpt-4o-mini", openapi_spec_path: str = ""):
        if not CEREBRAS_API_KEY:
            raise ValueError("Issue in Cerebras API Key!")

        try:
            #llm = ChatCerebras(model=model_name, temperature=0.5)
            # llm = CerebrasOpenAPIChat(
            #     cerebras_api_key=CEREBRAS_API_KEY,
            #     openapi_spec_path=openapi_spec_path
            # )
            llm = Cerebras()
            return llm
        except Exception:
            return None