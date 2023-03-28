import unittest
from main.main import Node, Stack
from main.custom_queue import Queue
from main.linked_list import LinkedList


class TestNode(unittest.TestCase):
    def test_Node(self):
        n1 = Node(5, None)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)

    def test_node_next_node(self):
        node1 = Node(10, None)
        node2 = Node(12, node1)
        self.assertEqual(node1.next_node, None)
        self.assertEqual(node2.next_node.data, 10)


class TestStack(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        self.assertEqual(stack.top, None)


    def test_push(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.top.next_node.data, 'data1')

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()
        self.assertEqual(stack.top.data, 'data1')


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')


    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.dequeue(), 'data3')
        self.assertEqual(queue.dequeue(), None)


class TestLinkedList(unittest.TestCase):
    def test_linked_list(self):
        ll = LinkedList()
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        lst = ll.to_list()
        self.assertEqual(lst[0]['id'], 0)
        self.assertEqual(lst[1]['id'], 1)
        self.assertEqual(lst[2]['id'], 2)


    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(ll.get_data_by_id(1), {'id': 1, 'username': 'lazzy508509'})
        self.assertEqual(ll.get_data_by_id(2), {'id': 2, 'username': 'mik.roz'})
        self.assertEqual(ll.get_data_by_id(4), None)
