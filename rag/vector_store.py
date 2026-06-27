import os
from langchain_chroma import Chroma
from utils.config_handler import chroma_config
from model.factory import embedding_model
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils.path_tool import get_abs_path
from utils.file_handler import pdf_loader, txt_loader, listdir_with_allowed_type, get_file_md5_hex
from utils.logger_handler import logger
from dotenv import load_dotenv
load_dotenv()

#Load local documents, split, embed, and store them in Chroma, 
# then expose a retriever for similarity search.
class VectorStoreService:
    def __init__(self):
        self.vector_store = Chroma(
            collection_name=chroma_config["collection_name"],
            embedding_function=embedding_model,
            persist_directory=chroma_config["persist_directory"],
        )

        self.spliter = RecursiveCharacterTextSplitter(
            chunk_size=chroma_config["chunk_size"], 
            chunk_overlap=chroma_config["chunk_overlap"],
            separators=chroma_config["separators"],
            length_function=len
        )


    def get_retriever(self):
        # Wrap the Chroma vector store as a LangChain retriever.
        # On query, it embeds the input text and returns the top_k most
        # similar document chunks. Used as the retrieval step in the RAG chain.
        return self.vector_store.as_retriever(
            search_kwargs={"k": chroma_config["top_k"]}
        )
    
    def load_document(self):
        # Load documents from the specified data path
        #
        
        def check_md5_hex(md5:str):
            if not os.path.exists(get_abs_path(chroma_config["md5_hex_store"])):
                # Create the file if it doesn't exist
                with open(get_abs_path(chroma_config["md5_hex_store"]), 'w', encoding='utf-8') as f:
                    pass  # Just create an empty file
                return False
            
            #if exists, check if the md5 is in the file
            with open(get_abs_path(chroma_config["md5_hex_store"]), 'r', encoding='utf-8') as f:
                md5_list = f.read().splitlines()
                for existing_md5 in md5_list:
                    if md5 == existing_md5: 
                        return True
                return False

        def save_md5_hex(md5:str):
            with open(get_abs_path(chroma_config["md5_hex_store"]), 'a', encoding='utf-8') as f:
                f.write(md5 + '\n')


        def get_file_documents(data_path):
            if data_path.endswith(".txt"):
                return txt_loader(data_path)
            
            if data_path.endswith(".pdf"):
                return pdf_loader(data_path)
            
            return []
        
        allowed_file_path: tuple[str] = listdir_with_allowed_type(
            chroma_config["data_path"],
            tuple(chroma_config["allow_file_type"])
        )

        
        for path in allowed_file_path: 
            #get md5 of the path
            md5_hex = get_file_md5_hex(path)

            if check_md5_hex(md5_hex):
                logger.info(f"{path} has exist")
                continue
                
            try: ## Load every documents
                documents: list[Document] = get_file_documents(path)

                if not documents:
                    logger.warning(f"{path} is invalid")
                    continue
                
                #split
                split_document : list[Document] = self.spliter.split_documents(documents)

                if not split_document:
                    logger.warning(f"{path} after split, there is no valid content")
                    continue
                
                #embed and store them in Chroma
                self.vector_store.add_documents(split_document)

                save_md5_hex(md5_hex)
                logger.info(f"{path} has load successfully")
            
            except Exception as e:
                logger.error(f"{path} load failed", exc_info=True)



if __name__ == '__main__':
    vs = VectorStoreService()

    vs.load_document()
    retriever = vs.get_retriever()

    res = retriever.invoke("迷路")
    for r in res:
        print(r.page_content)
        print("_"*20)