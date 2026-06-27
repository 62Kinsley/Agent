from utils.config_handler import prompt_config
from utils.path_tool import get_abs_path

def load_system_prompt():
    #check if the prompt_config has the key 'main_prompt', and get the path of the system prompt file
    try:
        system_prompt_path = get_abs_path(prompt_config['main_prompt'])
    except KeyError as e:
        logger.error(f"KeyError: {e}. Please check the prompt configuration.")
        raise  e

    #read the system prompt file and return the content
    try:
        with open(system_prompt_path, 'r', encoding='utf-8') as f:
            system_prompt = f.read()
    except FileNotFoundError:
        logger.error(f"File not found: {system_prompt_path}. Please check the file path.")
    except Exception as e:
        logger.error(f"Error reading system prompt: {e}")
        raise  e

    return system_prompt



def load_rag_prompt():
    try:
        rag_prompt_path = get_abs_path(prompt_config['rag_prompt'])
    except KeyError as e:
        logger.error(f"KeyError: {e}. Please check the rag configuration.")
        raise  e

    try:
        with open(rag_prompt_path, 'r', encoding='utf-8') as f:
            rag_prompt = f.read()
    except FileNotFoundError:
        logger.error(f"File not found: {rag_prompt_path}. Please check the file path.")
    except Exception as e:
        logger.error(f"Error reading rag prompt: {e}")
        raise  e

    return rag_prompt



def load_report_prompt():
    try:
        report_prompt_path = get_abs_path(prompt_config['report_prompt'])
    except KeyError as e:
        logger.error(f"KeyError: {e}. Please check the report configuration.")
        raise  e

    try:
        with open(report_prompt_path, 'r', encoding='utf-8') as f:
            report_prompt = f.read()
    except FileNotFoundError:
        logger.error(f"File not found: {report_prompt_path}. Please check the file path.")
    except Exception as e:
        logger.error(f"Error reading report prompt: {e}")
        raise  e

    return report_prompt

  
if __name__ == "__main__":
    system_prompt = load_system_prompt()
    print("System Prompt:")
    print(system_prompt)
