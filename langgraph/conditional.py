from typing import Dict, TypedDict, List
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
	number1: int
	operation: str
	number2: int
	finalNumber: int


def adder(state: AgentState) -> AgentState:
	"""This node adds the 2 numbers"""
	state["finalNumber"]= state["number1"]+state["number2"]
	return state


def subtractor(state:AgentState)-> AgentState:
	"""This node subtract the 2 numbers"""
	state["finalNumber"]= state["number1"] - state["number2"]
	return state


def decide_next_node(state: AgentState) -> AgentState:
	"""This is node will select the next node of the graph"""

	if state["operation"] == "+":
		return "addition_operation"
	elif state["operation"] == "-":
		return "subtraction_operation"
	

graph = StateGraph(AgentState)

graph.add_node("add_node",adder)
graph.add_node("subtract_node", subtractor)
graph.add_node("router", lambda state:state) # passthrough function

graph.add_edge(START,"router")

graph.add_conditional_edges(
	"router",
	decide_next_node,
	{
		# Edge: Node
		"addition_operation": "add_node",
		"subtraction_operation": "subtract_node"
	}

)

graph.add_edge("add_node",END)
graph.add_edge("subtract_node",END)

app = graph.compile()

# visualize the graph
print(app.get_graph().draw_ascii())


init_state = AgentState(number1=10,operation="-",number2=2)

print(app.invoke(init_state))