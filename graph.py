from dataclasses import dataclass, field
from typing import List, Dict, Set


@dataclass(repr=False)
class Node:
    year: str = field(default="")
    name: str = field(default="")
    creator: str = field(default="")
    predecessors: Set[str] = field(default_factory=set)
    predecessor_nodes: Set["Node"] = field(default_factory=set)

    @property
    def id(self) -> str:
        return self.year + self.name

    __str__ = __repr__ = lambda self: f"{self.name} ({self.year})"

    __eq__ = lambda self, other: self.id == other.id

    __lt__ = lambda self, other: self.id < other.id

    __le__ = lambda self, other: self.id <= other.id

    __gt__ = lambda self, other: self.id > other.id

    __ge__ = lambda self, other: self.id >= other.id


def has_matching_name(name: str, ancestor_candidate: str) -> bool:
    # use_exact_match = len(ancestor_candidate) <= 3 or len(name) <= 3

    # matches = False
    # if use_exact_match:
    #     matches = ancestor_candidate == name
    # else:
    #     matches = name.lower() in ancestor_candidate.lower()

    matches = ancestor_candidate == name

    return matches


def build_graph(objs: List[Dict]) -> List[Node]:
    nodes = [Node(**obj) for obj in objs]
    nodes.sort()

    for lang in nodes:
        lang_predecessor_nodes = []
        for pred in lang.predecessors:
            for other in nodes:
                if lang.id == other.id:
                    continue
                if has_matching_name(pred, other.name):
                    lang_predecessor_nodes.append(other)
        lang.predecessor_nodes = lang_predecessor_nodes

    return nodes
