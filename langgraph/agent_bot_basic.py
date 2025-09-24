from typing import Dict, TypedDict, List
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()


class AgentState(TypedDict):
	messages: List[HumanMessage]


llm = ChatGoogleGenerativeAI(model = "models/gemini-2.5-flash")


def process(state: AgentState) -> AgentState:
	"""Process the user message"""
	response = llm.invoke(state["messages"])
	print(f"\nAI: {response.content}")
	return state



graph = StateGraph(AgentState)

graph.add_node("process", process)
graph.add_edge(START,"process")
graph.add_edge("process",END)

app = graph.compile()


user_input = input("Enter: ")
while user_input != "exit":
	app.invoke({"messages": [HumanMessage(content=user_input)]})
	user_input = input("Enter: ")