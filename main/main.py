class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        """
        Добавляет данные в узел
        """
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """удаляет из стека верхний элемент и возвращает данные удаленного экземпляра класса Node"""
        remove = self.top
        if self.top is None:
            return None
        self.top = self.top.next_node
        return remove.data


if __name__ == '__main__':
    # n1 = Node(5, None)
    # n2 = Node('a', n1)
    # print(n1.data)
    # print(n2.data)
    # print(n1)
    # print(n2.next_node)
    #
    # stack = Stack()
    # stack.push('data1')
    # stack.push('data2')
    # stack.push('data3')
    # print(stack.top.data)
    # print(stack.top.next_node.data)
    # print(stack.top.next_node.next_node.data)
    # print(stack.top.next_node.next_node.next_node)
    # print(stack.top.next_node.next_node.next_node.data)
    # stack = Stack()
    # stack.push('data1')
    # data = stack.pop()
    #
    # # стэк стал пустой
    # print(stack.top)
    # print(data)
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()

    # print(stack.top.data)
    #
    # print(data)
