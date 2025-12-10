import uuid

GRAPHS = {}
RUNS = {}


def save_graph(graph):
    graph_id = str(uuid.uuid4())
    GRAPHS[graph_id] = graph
    return graph_id


def get_graph(graph_id):
    return GRAPHS.get(graph_id)


def save_run(run_id, data):
    RUNS[run_id] = data


def get_run(run_id):
    return RUNS.get(run_id)
