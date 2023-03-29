class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Хранит ссылку на начало связанного списка и на его конец"""
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


    def insert_beginning(self, data):
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node


    def insert_at_end(self, data):
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node


    def print_ll(self):
        """Вывод в консоль данных из односвязанного списка"""
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)

    def to_list(self):
        """Возвращает список с данными, содержащимися в односвязном списке LinkedList"""
        list_data = []
        current = self.head
        while current:
            list_data.append(current.data)
            current = current.next_node
        return list_data


    def get_data_by_id(self, id):
        """Возвращает первый найденный в LinkedList словарь с ключом id,
           значение которого равно переданному в метод значению."""
        current = self.head
        while current is not None:
            try:
                if current.data['id'] == id:
                    return current.data
                    break
            except TypeError:
                print('Данные не являются словарем или в словаре нет id')
            current = current.next_node

# ll = LinkedList()
# ll.insert_beginning({'id': 1})
# ll.insert_at_end({'id': 2})
# ll.insert_at_end({'id': 3})
# ll.insert_beginning({'id': 0})
# ll.print_ll()

ll = LinkedList()

ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
ll.insert_beginning({'id': 0, 'username': 'serebro'})

lst = ll.to_list()
for item in lst: print(item)

user_data = ll.get_data_by_id(3)
print(user_data)

ll = LinkedList()
ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
ll.insert_at_end('idusername')
ll.insert_at_end([1, 2, 3])
ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

user_data = ll.get_data_by_id(2)
print(user_data)

