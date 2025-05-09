from langchain_ollama import ChatOllama
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType

from tools import Toolchain

llm = ChatOllama(model="gemma3:12b")

tools = [
    Tool(
        name="create directory",
        func=Toolchain.create_directory,
        description="Creates a directory. Input should be a string with the directory name."
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def collect():
    request = input("> ")
    response = agent.invoke(request, verbose=False)

    print(response["output"])
    collect()

print("FS Agent - Created by Harvey Coombs - https://harveycoombs.com")
collect()