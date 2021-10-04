import constants
import bisect

MAX = constants.MAX


class leafNode:
    def __init__(self, parent=None, brother=None, key=-float("inf")):
        self.isLeaf = True
        self.parent = parent
        self.keys = []  # [-float("inf")]
        self.brother = brother
        self.cnt = 0
        self.first = key

    def set(self):
        self.first = self.keys[0]
        self.cnt = len(self.keys)

    def search(self, key):
        ok = 0
        ng = self.cnt
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if self.keys[mid] <= key:
                ok = mid
            else:
                ng = mid

        return ok

    def split(self):
        left_keys = self.keys[: MAX // 2]
        right_keys = self.keys[MAX // 2 :]
        self.keys = left_keys
        self.set()

        right = leafNode()
        right.keys += right_keys
        right.set()

        self.brother = right
        self.parent.add(right)

        return

    def add(self, key):
        if self.cnt == MAX:
            self.split()
            if self.brother.first <= key:
                self.brother.add(key)
            else:
                self.add(key)
        else:
            bisect.insort_left(self.keys, key)
            self.set()
        return
