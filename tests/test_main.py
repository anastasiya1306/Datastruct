import unittest
from main.main import Node, Stack

class TestNode(unittest.TestCase):
    def test_node_init(self):
        node1 = Node(10)
        assert node1.data == 10
        assert node1.next_node is None

    def test_node_next_node(self):
        node1 = Node(10)
        node2 = Node(120, node1)
        assert node2.next_node is node1


class TestStack(unittest.TestCase):
    def test_push(self):
