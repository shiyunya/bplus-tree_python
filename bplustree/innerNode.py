from . import constants
from . import Node
import bisect
import logging

logger = logging.getLogger(__name__)
MAX = constants.MAX


class innerNode(Node.Node):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.children = []

    def split(self):
        half = self.cnt // 2

        left = self
        right = innerNode()

        left_keys = self.keys[:half]
        right_keys = self.keys[half:]
        left_chidlren = self.children[:half]
        right_chidlren = self.children[half:]

        if self.parent is None:
            # Node is root
            logger.debug("B+tree LEVEL UP!!")
            self.__init__()

            left = innerNode()
            left.children = left_chidlren
            left.keys = left_keys
            left.update()
            for child in left.children:
                child.parent = left

            right.children = right_chidlren
            right.keys = right_keys
            right.update()
            for child in right.children:
                child.parent = right

            self.add(left)
            self.add(right)
            self.update()

        else:
            self.keys = left_keys
            self.children = left_chidlren
            self.update()

            right.keys = right_keys
            right.children = right_chidlren
            right.update()
            for child in right.children:
                child.parent = right
            self.parent.add(right)

        return left, right

    def merge(self):
        return

    def add(self, child):
        if self.cnt == MAX:
            left, right = self.split()
            if child.first < right.first:
                left.add(child)
            else:
                right.add(child)
        else:
            key = child.first
            idx = bisect.bisect_left(self.keys, key)
            self.keys.insert(idx, key)
            self.children.insert(idx, child)
            self.update()
            child.parent = self

        return
