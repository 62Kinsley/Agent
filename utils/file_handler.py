import os, hashlib
from utils.logger_handler import logger
from langchain_core.documents import Document
from langchain.document_loaders import PyPDFLoader, TextLoader

def get_file_md5_hex(filepath:str):
    if not os.path.exists(filepath):
        logger.error(f"File not found: {filepath}")
        return
    if not os.path.isfile(filepath):
        logger.error(f"Path is not a file: {filepath}")
        return
    
    md5_obj = hashlib.md5()

    chunk_size = 4096  # 4KB
    try:
        with open(filepath,'rb') as f: #	read binary mode
            while chunk := f.read(chunk_size):
                md5_obj.update(chunk)


            md5_hex = md5_obj.hexdigest()
            return md5_hex
    except Exception as e:
        logger.error(f"Error reading file {filepath}: {e}")
        return None

def listdir_with_allowed_type(path:str, allowed_types: tuple[str]): 
    #return a list of files with allowed types in the given directory
    files = []

    if not os.path.isdir(path):
        logger.error(f"Path is not a directory: {path}")
        return allowed_types
    
    for f in os.listdir(path):
        if f.endswith(allowed_types):
            files.append(os.path.join(path, f))
    
    return tuple(files)


def pdf_loader(fileath: str, passwd=None) -> list[Document]:
    return PyPDFLoader(fileath, passwd).load()



def txt_loader()-> list[Document]:
    return TextLoader(fileath, passwd).load()
