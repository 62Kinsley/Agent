#user ask question, search chromadb,  put question and answer and prompt to model
from rag.vector_store import VectorStoreService
from utils.prompt_loader import load_rag_prompt
from langchain_core.prompts import PromptTemplate
from model.factory import chat_model, embedding_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from utils.logger_handler import logger

class RagSummerizeService(object):
    def __init__(self):
        self.vector_store = VectorStoreService()
        self.retriever = self.vector_store.get_retriever()
        self.prompt_text = load_rag_prompt()
        self.prompt_template = PromptTemplate.from_template(self.prompt_text)
        self.model = chat_model
        self.chain = self.__init__chain()

    def __init__chain(self):
        chain = self.prompt_template | self.model | StrOutputParser()
        return chain
    
    def retriever_docs(self, query:str) -> list[Document]:
        return self.retriever.invoke(query)
    
    def rag_summerize(self, query:str) -> str:
        context_docs = self.retriever_docs(query)    

        context = ""
        counter = 0
        for doc in context_docs:
            counter += 1
            context += f"[refer{counter} : refer {doc.page_content} | metadata:{doc.metadata}\n]"
    
        return self.chain.invoke(
            {
                "input" : query,
                "context": context,
            }
        )

if __name__ == '__main__':
    rag = RagSummerizeService()

    print(rag.rag_summerize("大户适合那些扫地机器人？"))