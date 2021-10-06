import constants
import innerNode
import leafNode
from collections import deque
from random import randint

MAX = constants.MAX


class Btree:
    def __init__(self, key=-float("inf")):
        root = innerNode.innerNode()
        self.root = root
        leaf = leafNode.leafNode(key=key)
        leaf.parent = root
        self.root.add(leaf)

    def getLeaf(self, key):
        now = self.root
        while not now.isLeaf:
            idx = now.search(key)
            now = now.children[idx]
        return now

    def add(self, key, value=None):
        now = self.getLeaf(key)
        now.add(key, value)

    def predecessor(self, key):
        now = self.getLeaf(key)
        return now.predecessor(key)

    def print(self):
        print("-" * MAX, "B+tree", "-" * MAX)

        q = deque([(self.root, 0)])
        now, level = q.popleft()
        print("LEVEL", level, "ROOT :", now.keys)
        for i in range(now.cnt):
            q.append((now.children[i], level + 1))

        while q:
            now, level = q.popleft()
            node_type = "LEAF" if now.isLeaf else "INNER"
            print("LEVEL", level, node_type + " :", now.keys)

            if now.isLeaf:
                continue
            for i in range(now.cnt):
                q.append((now.children[i], level + 1))


def main():
    bt = Btree()

    for i in range(1000):
        bt.add(randint(0, 10000))

    bt.print()

    for i in range(10):
        key = randint(0, 10000)
        print(key, bt.predecessor(key))
    return


if __name__ == "__main__":
    main()
