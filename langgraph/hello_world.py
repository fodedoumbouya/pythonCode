from typing import Dict, TypedDict
from langgraph.graph import StateGraph

# Define the structure of the input using TypedDict to keep tack of information. State

class AgentState(TypedDict): # State schema
	message: str


# let's create a greeting node
def greeting_node(state: AgentState) -> AgentState:
	"""Simple node that adds a greeting message to the state."""
	state["message"] = "Hey " + state["message"] + ", welcome to LangGraph!"
	return state




# Create the state graph. it's the graph that will hold all the nodes and the state schema
graph =  StateGraph(AgentState)

# Add the greeting node to the graph
graph.add_node("greeter", greeting_node)

# let's set the start node
graph.set_entry_point("greeter")

# add finish node
graph.set_finish_point("greeter")

# let's compile the graph

app = graph.compile()
# visualize the graph
print(app.get_graph().draw_ascii())


result = app.invoke({"message": "John"})

print(result["message"] )


