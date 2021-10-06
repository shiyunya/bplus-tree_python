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

    def upsert(self, key, value=None):
        now = self.getLeaf(key)
        now.upsert(key, value)

    def delete(self, key):
        now = self.getLeaf(key)
        now.delete(key)

    def predecessor(self, key):
        now = self.getLeaf(key)
        return now.predecessor(key)

    def range(self, first, end):
        now = self.getLeaf(first)
        ans = []

        while now.first <= end:
            for i in range(now.cnt):
                if now.keys[i] < first:
                    continue
                if now.keys[i] <= end:
                    ans.append((now.keys[i], now.values[i]))
                else:
                    break
            else:
                if now.brother is not None:
                    now = now.brother
                    continue
                else:
                    break
            break

        return ans

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
        key = randint(0, 10000)
        value = randint(0, 10000)
        bt.upsert(key, value)

    bt.print()

    for i in range(10):
        key = randint(0, 10000)
        print(key, bt.predecessor(key))

    for i in range(10):
        key = randint(0, 10000)
        first = max(0, key - 500)
        end = min(10000, key + 500)
        ans = bt.range(first, end)
        print("range [", first, ",", end, "]:")
        print(ans)
        print()

    return


if __name__ == "__main__":
    main()
