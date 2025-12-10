from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import uuid

app = FastAPI()

# In-memory graph storage
GRAPHS = {}


# ---------- MODELS ----------
class GraphCreate(BaseModel):
    nodes: Dict[str, str]
    edges: Dict[str, str]
    start_node: str


class GraphRun(BaseModel):
    graph_id: str
    initial_state: Dict[str, int]


# ---------- ROUTES ----------
@app.get("/")
def root():
    return {"message": "API is running"}


@app.post("/graph/create")
def create_graph(data: GraphCreate):
    graph_id = str(uuid.uuid4())

    GRAPHS[graph_id] = {
        "nodes": data.nodes,
        "edges": data.edges,
        "start_node": data.start_node
    }

    return {
        "graph_id": graph_id,
        "message": "Graph created successfully"
    }


@app.post("/graph/run")
def run_graph(data: GraphRun):
    graph = GRAPHS.get(data.graph_id)

    if graph is None:
        raise HTTPException(status_code=404, detail="Graph not found")

    # Simple fake execution logic
    current_node = graph["start_node"]
    quality = data.initial_state.get("quality_score", 0)
    threshold = data.initial_state.get("threshold", 100)

    while quality < threshold and current_node in graph["edges"]:
        quality += 10
        current_node = graph["edges"][current_node]

    return {
        "final_node": current_node,
        "final_quality": quality
    }
