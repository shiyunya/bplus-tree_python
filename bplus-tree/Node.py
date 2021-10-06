import constants

MAX = constants.MAX


class Node:
    def __init__(self, parent=None, brother=None, key=-float("inf")):
        self.isLeaf = False
        self.parent = parent
        self.keys = []
        self.brother = brother
        self.cnt = 0
        self.first = key

    def update(self):
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
