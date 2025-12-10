def extract_functions(state):
    code = state.get("code", "")
    lines = code.split("\n")

    functions = []
    for line in lines:
        if line.strip().startswith("def "):
            functions.append(line.strip())

    state["functions"] = functions
    state["function_count"] = len(functions)
    return state


def check_complexity(state):
    code = state.get("code", "")
    lines = code.split("\n")

    complexity = len(lines) + state.get("function_count", 0) * 5
    state["complexity"] = complexity
    return state


def detect_issues(state):
    issues = []

    if state.get("complexity", 0) > 100:
        issues.append("Code is too complex")

    state["issues"] = issues
    return state


def suggest_improvements(state):
    quality = state.get("quality_score", 50)

    if len(state.get("issues", [])) == 0:
        quality += 10
    else:
        quality -= 5

    state["quality_score"] = quality
    return state


def should_continue(state):
    return state.get("quality_score", 0) < state.get("threshold", 80)
