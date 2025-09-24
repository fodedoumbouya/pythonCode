from typing import Annotated, Sequence, TypedDict
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage # The funcdational class for all message types in LangGraph
from langchain_core.messages import ToolMessage # Passes data back to LLM after it calls a tool such as the content and the tool_call_id
from langchain_core.messages import SystemMessage # Message for providing instrcution to the LLM
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END, START
from langgraph.prebuilt import ToolNode


load_dotenv()


class AgentState(TypedDict):
	messages: Annotated[Sequence[BaseMessage],add_messages]
	# Annotated help us add meta data to the data
	# so here our data type is Sequence[BaseMessage] and the metadata is add_messages


# Creating a tool in python. we need @tool annotation

@tool
def add(a: int, b:int):
	"""This is an addition functiion that adds 2 numbers together"""
	return a+b

@tool 
def multiple(a: int, b: int):
	"""this function does multiplication"""
	return a*b

tools = [add,multiple]
model =  ChatGoogleGenerativeAI(model = "models/gemini-2.5-flash").bind_tools(tools=tools)

def model_call(state: AgentState)-> AgentState:
	system_prompt = SystemMessage(content=
			       "You are my AI assistant, please answer my query to the best of your ability"
			       )
	response = model.invoke([system_prompt] + state["messages"])
	return {"messages":[response]}


def should_continue(state: AgentState)->AgentState:
	messages = state["messages"]
	last_message = messages[-1]
	if not last_message.tool_calls:
		return "end"
	else:
		return "continue"
	


graph = StateGraph(AgentState)
graph.add_node("our_agent", model_call)

tool_node = ToolNode(tools=tools)
graph.add_node("tools",tool_node)

graph.add_edge(START,"our_agent")


graph.add_conditional_edges(
	"our_agent",
	should_continue,
	{
		"end": END,
		"continue": "tools"
	}
)

graph.add_edge("tools","our_agent")


app = graph.compile()

# visualize the graph
print(app.get_graph().draw_ascii())

def print_stream(stream):
	for s in stream:
		message = s["messages"][-1]
		if isinstance(message, tuple):
			print(f"tuple message [{message}]")
		else:
			message.pretty_print()



inputs = {"messages": [("user","add 30 + 12, add 20+ 10 and then multiply the first result by 7. also tell me a joke please")]}
print_stream(app.stream(input=inputs, stream_mode="values"))