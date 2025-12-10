# AI-WORKFLOW-AGENT-TREDENCE-
This project is a simple workflow engine built using FastAPI. It allows workflows to be defined as a graph with nodes and edges and then executed step by step using an initial state. The goal of this project is to demonstrate how basic agent-style workflows can be created, run, and tested through API endpoints in a clean and easy-to-understand way.

How the Project Works 

This project is a simple workflow engine built using FastAPI where a workflow is represented as a graph made up of nodes and edges. Each node represents a step in the workflow, and edges define the flow between these steps. First, a workflow graph is created using an API by providing the nodes, edges, and a starting node. Once the graph is created, it is stored in memory and assigned a unique graph ID. This graph ID is then used to run the workflow by passing an initial state to another API endpoint. The workflow engine processes the graph step by step based on the defined edges and returns the final result after execution.

How to Run the Project (Step by Step)

1)Open the project folder in VS Code.

2)Make sure Python is installed on your system.

3)Install the required dependencies by running:
    pip install -r requirements.txt
    
4)Start the FastAPI server using Uvicorn:
    uvicorn app.main:app --reload
    
5)Open a web browser and go to:
    http://127.0.0.1:8000/docs
    this will take you to interactive swagger UI where you can test api usage.
    
6)Use Swagger UI to first create a workflow using the /graph/create API and then run the workflow using the /graph/run API.
## 🧪 Example API Usage

### A) Create Graph

**Request**
```json
{
  "nodes": {
    "check": "check_quality",
    "improve": "improve_quality"
  },
  "edges": {
    "check": "improve"
  },
  "start_node": "check"
}

Example Response

{
  "graph_id": "generated-graph-id",

  "message": "Graph created successfully"
}

B)RUN THE GRAPH

Example Request

{
  "graph_id": "PASTE_GRAPH_ID_HERE",
  
  "initial_state": {
    "quality_score": 50,  
    "threshold": 80
  }
}

Example Response

{
  "final_node": "improve",
  
  "final_quality": 60
}
    
