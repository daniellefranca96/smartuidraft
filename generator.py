from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.memory.chat_memory import ChatMessageHistory
from langchain.schema.messages import BaseMessage
from dotenv import load_dotenv
import re
import os

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv(key="OPENAI_API_KEY")

llm = ChatOpenAI(model=os.getenv("MODEL", "gpt-3.5-turbo-0613"))

master_memory = ConversationBufferWindowMemory(k=2, memory_key="history")

prompt = 'You are a Web UI designer. Users will describe their desired user interface, and you will craft it using HTML, CSS, and JavaScript. Provide only the complete UI code all in one file. Focus on creating a single page per request. Here is the history of previous interactions, use its generations as base to follow next requests: [{history}]'
system = SystemMessagePromptTemplate.from_template(prompt)
user =  HumanMessagePromptTemplate.from_template('{request}')
chat_prompt_template = ChatPromptTemplate.from_messages([system, user])
chain = LLMChain(llm=llm, prompt=chat_prompt_template, memory=master_memory)


def generate_code(request):
    code = chain.run(request)
    code = extract_html(code)
    return code
    
def get_last_code(memory: dict):
    return memory

def extract_html(content):
    pattern = re.compile(r'<html.*?>(.*?)</html>', re.DOTALL | re.IGNORECASE)
    match = pattern.search(content)
    if match:
        return match.group(1)
    return None
    

