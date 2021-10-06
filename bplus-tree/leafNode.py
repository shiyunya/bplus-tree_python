import constants
import Node
import bisect

MAX = constants.MAX


class leafNode(Node.Node):
    def __init__(self, parent=None, brother=None, key=-float("inf")):
        super().__init__(parent=parent, brother=brother, key=key)
        self.isLeaf = True
        self.values = []

    def set(self):
        self.first = self.keys[0]
        self.cnt = len(self.keys)

    def split(self):
        half = MAX // 2
        left_keys = self.keys[:half]
        right_keys = self.keys[half:]
        left_values = self.values[:half]
        right_values = self.values[half:]

        self.keys = left_keys
        self.values = left_values
        self.set()

        right = leafNode()
        right.keys = right_keys
        right.values = right_values
        right.set()

        self.brother = right
        self.parent.add(right)

        return

    def add(self, key, value=None):
        if self.cnt == MAX:
            self.split()
            if self.brother.first <= key:
                self.brother.add(key, value)
            else:
                self.add(key, value)
        else:
            idx = bisect.bisect_left(self.keys, key)
            self.keys.insert(idx, key)
            self.values.insert(idx, value)
            self.set()
        return

    def predecessor(self, key):
        idx = self.search(key)
        return (self.keys[idx], self.values[idx])
