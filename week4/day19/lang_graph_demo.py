from langgraph.graph import END
from langgraph.graph import StateGraph
from typing import TypedDict

class State(TypedDict):
    number : int

def double(state:State) -> dict:
    boardnum = state["number"]
    newnum = boardnum*2
    print("Number is doubled")
    return {"number":newnum}

def finish(state:State) -> dict:
    boardnum = state["number"]
    print(boardnum)
    return {"number":boardnum}

def decission(state:State) -> str:
    if state["number"]>100:
        return "finish"
    else:
        return "double"

builder = StateGraph(State)

builder.add_node("Double",double)
builder.add_node("Finish",finish)

builder.set_entry_point("Double")

builder.add_conditional_edges(
    "Double",
    decission,
    {
        "double":"Double",
        "finish":"Finish"
    }
)

builder.add_edge("Finish",END)

graph=builder.compile()

if __name__ == "__main__":
    graph.invoke(
        {
            "number" : 3
        }
    )