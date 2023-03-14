class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """Добавляет данные в очередь"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node


    def dequeue(self):
        """Удаляет из очереди крайний левый элемент (первый добавленный)"""
        if self.head is None:
            return None
        else:
            dequeue_element = self.head
            self.head = self.head.next_node
            return dequeue_element.data

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    # # print(queue.head.data)
    # # print(queue.head.next_node.data)
    # # print(queue.tail.data)
    # # print(queue.tail.next_node)
    # # print(queue.tail.next_node.data)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())