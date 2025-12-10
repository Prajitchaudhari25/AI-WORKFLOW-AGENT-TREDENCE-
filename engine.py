from app import nodes

NODE_MAP = {
    "extract_functions": nodes.extract_functions,
    "check_complexity": nodes.check_complexity,
    "detect_issues": nodes.detect_issues,
    "suggest_improvements": nodes.suggest_improvements,
}


def run_graph(edges, start_node, state):
    current = start_node
    log = []

    while current:
        func = NODE_MAP[current]
        state = func(state)
        log.append(current)

        if current == "suggest_improvements":
            if nodes.should_continue(state):
                current = "check_complexity"
            else:
                break
        else:
            current = edges.get(current)

    return state, log
