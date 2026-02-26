import ftb_snbt_lib as slib

__all__ = ["BaseType", "ItemType", "ExperimentType", "AdvancementType", "Node", "Edge", "Graph"]

class BaseType:
    def encode_slib_compound(self) -> slib.Compound:
        raise NotImplementedError()

class ItemType(BaseType):
    __slots__ = ["item", "amount"]
    def __init__(self, item: str, amount: int):
        self.item = item
        self.amount = amount
    def encode_slib_compound(self) -> slib.Compound:
        result = slib.Compound()
        result["type"] = slib.String("item")
        result["item"] = slib.String(self.item)
        result["count"] = slib.Integer(self.amount)
        return result

class ExperimentType(BaseType):
    __slots__ = ["amount"]
    def __init__(self, amount: int):
        self.amount = amount
    def encode_slib_compound(self) -> slib.Compound:
        result = slib.Compound()
        result["type"] = slib.String("xp")
        result["count"] = slib.Integer(self.amount)
        return result

class AdvancementType(BaseType):
    __slots__ = ["advancement"]
    def __init__(self, advancement: str):
        self.advancement = advancement
    def encode_slib_compound(self) -> slib.Compound:
        result = slib.Compound()
        result["type"] = slib.String("advancement")
        result["advancement"] = slib.String(self.advancement)
        return result

class Node:
    __slots__ = ["uid", "name", "description", "tasks" , "rewards"]
    def __init__(self, uid: str, name: str, description: str, tasks: list[BaseType], rewards: list[BaseType]):
        self.uid = uid
        self.name = name
        self.description = description
        self.tasks = tasks
        self.rewards = rewards
    # We cannot encode here

class Edge:
    __slots__ = ["frm", "to"]
    def __init__(self, frm: int, to: int):
        self.frm = frm
        self.to = to

class Graph:
    __slots__ = ["name", "index", "nodes", "edges", "uid_to_node", "dependencies"]
    def __init__(self, name: str, index: int):
        self.name = name
        self.index = index
        self.nodes: list[Node] = []
        self.edges: list[Edge] = []
        self.uid_to_node: dict[str, int] = {}
        self.dependencies: list[list[int]] = []
    def add_node(self, node: Node):
        self.nodes.append(node)
        self.uid_to_node[node.uid] = len(self.nodes) - 1
        self.dependencies.append([])
    def add_edge(self, frm_uid: str, to_uid: str):
        frm_idx = self.uid_to_node[frm_uid]
        to_idx = self.uid_to_node[to_uid]
        self.edges.append(Edge(frm_idx, to_idx))
        self.dependencies[to_idx].append(frm_idx)
    def find_node(self, node_uid: str) -> Node:
        node_idx = self.uid_to_node[node_uid]
        return self.nodes[node_idx]