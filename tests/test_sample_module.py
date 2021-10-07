# coding=utf-8

from bplustree import Btree


def test_predecessor_query():
    bt = Btree.Btree()
    bt.upsert(1)
    bt.upsert(10)
    assert bt.predecessor(5)[0] == 1


def test_successor_query():
    bt = Btree.Btree()
    bt.upsert(1)
    bt.upsert(10)
    assert bt.successor(5)[0] == 10


def test_range_query():
    bt = Btree.Btree()
    bt.upsert(1)
    bt.upsert(5)
    bt.upsert(6)
    bt.upsert(10)
    assert len(bt.range(2, 9)) == 2
