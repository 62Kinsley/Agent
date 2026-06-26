from langchain.chroma import Chroma
from utils.config_handler import chroma_config

class VectorStoreService:
    def __init__(self):
        self.vector_store = Chroma(
            collection_name=chroma_config["collection_name"],
            embedding_function=embeddings,
            persist_directory=chroma_config["persist_directory"],
        )
        self.spliter = None

   