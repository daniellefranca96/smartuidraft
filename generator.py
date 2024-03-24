from langchain_openai.chat_models import ChatOpenAI
from langchain_community.llms import HuggingFaceEndpoint
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import BedrockChat
from prompt import MAIN_PROMPT
from dotenv import load_dotenv
from operator import itemgetter
from langchain_anthropic import ChatAnthropic
import re
import os

load_dotenv()
os.environ['LLM_PROVIDER'] = os.getenv("LLM_PROVIDER", "hugginfaces")
os.environ['ANTHROPIC_MODEL'] = os.getenv("ANTHROPIC_MODEL", "claude-3-haiku")
os.environ['OPENAI_MODEL'] = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
os.environ['GOOGLE_MODEL'] = os.getenv("GOOGLE_MODEL", "gemini-pro")
os.environ['BEDROCK_MODEL'] = os.getenv("BEDROCK_MODEL", "anthropic.claude-3-haiku-20240307-v1:0")
os.environ['HUGGINGFACEHUB_MODEL'] = os.getenv("HUGGINGFACEHUB", "mistralai/Mixtral-8x7B-Instruct-v0.1")
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")
os.environ['ANTHROPIC_API_KEY'] = os.getenv("ANTHROPIC_API_KEY")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.environ['AWS_KEY'] = os.getenv("AWS_KEY")
os.environ['AWS_SECRET'] = os.getenv("AWS_SECRET")

if os.environ['LLM_PROVIDER'].lower() == "openai":
    llm = ChatOpenAI(model_name=os.environ['OPENAI_MODEL'])
elif os.environ['LLM_PROVIDER'].lower() == "google":
    llm = ChatGoogleGenerativeAI(model=os.environ['GOOGLE_MODEL'])
elif os.environ['LLM_PROVIDER'].lower() == "hugginfaces":
    llm = HuggingFaceEndpoint(repo_id=os.environ['HUGGINGFACEHUB_MODEL'], max_new_tokens=20000)
elif os.environ['LLM_PROVIDER'].lower() == "bedrock":
    llm = BedrockChat(model_id=os.environ['BEDROCK_MODEL'], model_kwargs={"max_tokens": 5000})
elif os.environ['LLM_PROVIDER'].lower() == "anthropic":
    llm = ChatAnthropic(model=os.environ['ANTHROPIC_MODEL'], max_tokens=4096)

master_memory = ConversationBufferWindowMemory(k=2, memory_key="history")

prompt = PromptTemplate.from_template(MAIN_PROMPT)

chain = (
    RunnablePassthrough.assign(
        history=RunnableLambda(master_memory.load_memory_variables) | itemgetter("history")
    )
    | prompt
    | llm
    | StrOutputParser()
)


def generate_code(request, template):
    print(template)
    code = chain.invoke({"request": request, "template":template})
    print("Response: "+code)
    code = extract_html(code)
    master_memory.save_context({"input": request}, {"output": code})
    return code
    
def get_last_code(memory: dict):
    return memory

def extract_html(content):
    pattern = re.compile(r'<html.*?>(.*?)</html>', re.DOTALL | re.IGNORECASE)
    match = pattern.search(content)
    if match:
        return "<html>"+match.group(1)+"</html>"
    else:
        pattern = re.compile(r'<head.*?>(.*?)</body>', re.DOTALL | re.IGNORECASE)
        match = pattern.search(content)
        if match:
             return "<html>"+match.group(1)+"</html>"
    return ""
    

