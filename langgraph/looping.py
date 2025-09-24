from typing import Dict, TypedDict, List
from langgraph.graph import StateGraph, START, END
import random

class AgentState(TypedDict):
	name: str
	number: List[int]
	counter: int 


def greeting_node(state: AgentState) -> AgentState:
	"""Greeting Node which says hi to the person"""
	state["name"] = f"Hello, {state['name']}"
	state['counter'] = 0
	print(state)
	return state


def random_node(state: AgentState) -> AgentState:
	"""Generates a random number from 0 to 10"""

	state["number"].append(random.randint(0,10))
	state["counter"] +=1

	return state


def should_continue(state: AgentState) -> AgentState:
	"""Function to decide what to do next"""
	if state["counter"] <5:
		print("ENTERING LOOP", state["counter"])
		return "loop" #continue looping
	else:
		return "exit" #exit the loop
	

graph = StateGraph(AgentState)

graph.add_node("greeting",greeting_node)
graph.add_node("random", random_node)

graph.add_edge("greeting","random")

graph.add_conditional_edges(
	"random",
	should_continue,
	{
		"loop": "random",
		"exit": END
	}
)

graph.add_edge(START, "greeting")

app = graph.compile()

# visualize the graph
# print(app.get_graph().draw_ascii())

initState = AgentState(name="f",number=[],counter=0)

print(app.invoke(initState))