from typing import Dict, TypedDict, List, Union
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()


class AgentState(TypedDict):
	messages: List[Union[HumanMessage, AIMessage]]


llm = ChatGoogleGenerativeAI(model = "models/gemini-2.5-flash")

def process(state: AgentState) -> AgentState:
	"""Process the user message"""
	response = llm.invoke(state["messages"])
	state["messages"].append(AIMessage(content=response.content))
	print(f"\nAI: {response.content}")
	return state



graph = StateGraph(AgentState)

graph.add_node("process", process)
graph.add_edge(START,"process")
graph.add_edge("process",END)

app = graph.compile()

conversation_history = []

user_input = input("Enter: ")
while user_input != "exit":
	conversation_history.append(HumanMessage(content=user_input))
	result = app.invoke({"messages": conversation_history})
	print(result["messages"])
	conversation_history = result["messages"]
	user_input = input("Enter: ")