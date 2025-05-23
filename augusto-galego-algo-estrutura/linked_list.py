class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value):
        new_node = Node(value)

        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def add_to_end(self, value):
        new_node = Node(value)

        new_node.prev = self.tail

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def remove_from_front(self) -> Node:
        if not self.head:
            return None
        removed_node = self.head

        self.head = self.head.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return removed_node

    def remove_from_end(self) -> Node:
        if not self.tail:
            return None

        removed_node = self.tail

        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        return removed_node

    def print_list(self):
        current = self.head

        while current:
            print(current.value, end=", " if current.next else "\n")
            current = current.next


dll = DoublyLinkedList()

dll.add_to_front(1)  # adicionando 1 ao início
dll.add_to_front(2)  # adicionando 2 ao início
dll.add_to_front(3)  # adicionando 3 ao início
dll.add_to_end(4)    # adicionando 4 ao final
dll.add_to_end(5)    # adicionando 5 ao final

print("Lista após inserções:")
dll.print_list()  # Output: 3 <-> 2 <-> 1 <-> 4 <-> 5

print("Head value (esperado 3):", dll.head.value)
print("Tail value (esperado 5):", dll.tail.value)
print("Head.next.value (esperado 2):", dll.head.next.value)
print("Tail.prev.value (esperado 4):", dll.tail.prev.value)

print("\nRemovendo do início (esperado 3):", dll.remove_from_front().value)
print("Removendo do final (esperado 5):", dll.remove_from_end().value)

print("Lista após duas remoções:")
dll.print_list()  # Output: 2 <-> 1 <-> 4

print("Head value (esperado 2):", dll.head.value)
print("Tail value (esperado 4):", dll.tail.value)
print("Head.next.value (esperado 1):", dll.head.next.value)
print("Tail.prev.value (esperado 1):", dll.tail.prev.value)

print("\nRemovendo do início (esperado 2):", dll.remove_from_front().value)
print("Removendo do final (esperado 4):", dll.remove_from_end().value)

print("Lista após mais duas remoções:")
dll.print_list()  # Output: 1

print("\nRemovendo último item (esperado 1):", dll.remove_from_front().value)

print("Head após remover tudo (esperado None):", dll.head)
print("Tail após remover tudo (esperado None):", dll.tail)

print("Removendo de lista vazia (esperado None):", dll.remove_from_front())
print("Removendo de lista vazia (esperado None):", dll.remove_from_end())

print("Lista final (esperado vazia):")
dll.print_list()  # Output: None
