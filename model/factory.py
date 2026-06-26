from abc import ABC, abstractmethod
from typing import Optional
from langchain_core.embeddings import Embeddings
from langchain.chat_models.base import BaseChatModel
from langchain_qwq import ChatQwen
from langchain_openai import OpenAIEmbeddings
from utils.config_handler import rag_config, chroma_config, prompt_config, agent_config

class BaseModelFactory(ABC):#abstract base class
    @abstractmethod
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        pass

class ChatModelFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        return ChatQwen(
                    model=rag_config["chat_model_name"],
                    max_tokens=3_000,
                    timeout=None,
                    max_retries=2,
                )
    
class EmbeddingModelFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        return OpenAIEmbeddings(
                    model=rag_config["embedding_model_name"]
                    base_url=rag_config["base_url"],
                    api_key=rag_config["api_key"],
                )
    


chat_model = ChatModelFactory().generator()
embedding_model = EmbeddingModelFactory().generator()