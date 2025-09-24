from typing import Dict, TypedDict, List
from langgraph.graph import StateGraph



class AgentState(TypedDict):
	values: List[int]
	name: str
	result: str


def process_values(state: AgentState) -> AgentState:
	"""This function handlers multiple different inputs"""
	print(state)
	state["result"] = f"Hello {state['name']}! The sum is {sum(state['values'])}"
	print(state)
	return state


graph = StateGraph(AgentState)

graph.add_node("processor", process_values)

graph.set_entry_point("processor")
graph.set_finish_point("processor")

app = graph.compile()

# visualize the graph
print(app.get_graph().draw_ascii())


result = app.invoke({"values": [2,3,5,3],"name": "Fode"})

print(result)