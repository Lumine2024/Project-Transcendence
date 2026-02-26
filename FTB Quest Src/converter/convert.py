from .Graph import *
import ftb_snbt_lib as slib
from graphviz import Digraph
import networkx as nx
from collections import deque

__all__ = ["convert"]

g_id = 0
def generate_id() -> int:
    global g_id
    result = g_id
    g_id += 1
    return result

def auto_layout(graph: Graph) -> list[tuple[float, float]]:
    graph_nx = nx.DiGraph()
    for i in range(len(graph.nodes)):
        graph_nx.add_node(i)
    for edge in graph.edges:
        graph_nx.add_edge(edge.frm, edge.to)
    dot = Digraph(engine="dot")
    dot.attr(splines="line", rankdir="TB", nodesep="0.5", ranksep="0.75")
    for node in graph_nx.nodes():
        dot.node(str(node))
    for frm, to in graph_nx.edges():
        dot.edge(str(frm), str(to))
    plain = dot.pipe(format="plain").decode("utf-8")
    result: list[tuple[float, float]] = [(0.0, 0.0) for _ in range(len(graph.nodes))]
    for line in plain.splitlines():
        parts = line.split()
        if len(parts) >= 4 and parts[0] == "node":
            index = int(parts[1])
            x = float(parts[2])
            y = float(parts[3])
            result[index] = (x, y)
    return result

def toposort(graph: Graph) -> list[int]:
    node_count = len(graph.nodes)
    indegree = [len(graph.dependencies[i]) for i in range(node_count)]
    children: list[list[int]] = [[] for _ in range(node_count)]

    for node_idx, deps in enumerate(graph.dependencies):
        for dep_idx in deps:
            children[dep_idx].append(node_idx)

    queue = deque([idx for idx in range(node_count) if indegree[idx] == 0])
    order: list[int] = []

    while queue:
        current = queue.popleft()
        order.append(current)
        for child in children[current]:
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)

    if len(order) != node_count:
        raise ValueError("The graph is not a DAG")

    return order

def convert(graph: Graph) -> slib.Compound:
    layout = auto_layout(graph)
    result = slib.Compound()
    result["default_hide_dependency_lines"] = slib.Bool(False)
    result["default_quest_shape"] = slib.String("")
    result["filename"] = slib.String(graph.name.replace(" ", "_"))
    result["id"] = slib.String(format(generate_id(), "016x"))
    result["title"] = slib.String(graph.name)
    result["group"] = slib.String("")
    result["quest_links"] = slib.List([])
    result["order_index"] = slib.Integer(graph.index)
    quests: list[slib.Compound] = []
    ids: list[int] = [0] * len(graph.nodes)
    for i in toposort(graph):
        node = graph.nodes[i]
        x, y = layout[i]
        dependencies = graph.dependencies[i]
        id = generate_id()
        ids[i] = id
        quest = slib.Compound()
        quest["id"] = slib.String(format(id, "016x"))
        quest["title"] = slib.String(node.name)
        quest["subtitle"] = slib.String(node.description)
        quest["dependencies"] = slib.List([slib.String(format(ids[dependency], "016x")) for dependency in dependencies])
        quest["tasks"] = slib.List([task.encode_slib_compound() for task in node.tasks])
        quest["rewards"] = slib.List([reward.encode_slib_compound() for reward in node.rewards])
        quest["x"] = slib.Double(x)
        quest["y"] = slib.Double(y)
        quests.append(quest)
    result["quests"] = slib.List(quests)
    return result

