import yaml
from utils.path_tool import get_abs_path


#convert yaml config file to python dict
def load_rag_config(config_path: str = get_abs_path("config/rag.yaml"), encoding: str = 'utf-8'):  
    with open(config_path, 'r', encoding=encoding) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config


def load_chroma_config(config_path: str = get_abs_path("config/chroma.yaml"), encoding: str = 'utf-8'):  
    with open(config_path, 'r', encoding=encoding) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config


def load_prompt_config(config_path: str = get_abs_path("config/prompt.yaml"), encoding: str = 'utf-8'):  
    with open(config_path, 'r', encoding=encoding) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config

def load_agent_config(config_path: str = get_abs_path("config/agent.yaml"), encoding: str = 'utf-8'):  
    with open(config_path, 'r', encoding=encoding) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config


rag_config = load_rag_config()
chroma_config = load_chroma_config()
prompt_config = load_prompt_config()
agent_config = load_agent_config()



if __name__ == "__main__":
    print(agent_config["chat_model_name"])