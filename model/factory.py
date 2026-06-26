from abc import ABC, abstractmethod
from typing import Optional
from langchain_core.embeddings import Embeddings
from langchain.chat_models.base import BaseChatModel
from langchain_qwq import ChatQwen

llm = ChatQwen(
    model="qwen-flash",
    max_tokens=3_000,
    timeout=None,
    max_retries=2,
    # other params...
)

class BaseModelFactory(ABC):
    @abstractmethod
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        pass