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

    def hasCycle(self, head: Node):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


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


# testando ciclo
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # criando um ciclo
dll_with_cycle = DoublyLinkedList()
dll_with_cycle.head = node1
print("\nTeste de ciclo na lista:")
print("Lista tem ciclo?", dll_with_cycle.hasCycle(
    dll_with_cycle.head))  # Output: True

# Note: The cycle detection method will not print the list correctly due to the cycle.
# To avoid infinite loop in printing, we should not print the list with a cycle.
# The cycle detection method is only for checking if a cycle exists, not for printing the list.
# The above code demonstrates the functionality of a doubly linked list,
# including adding and removing nodes, and checking for cycles.

# testando lista sem ciclo
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
dll_without_cycle = DoublyLinkedList()
dll_without_cycle.head = node1
print("\nTeste de ciclo na lista sem ciclo:")
print("Lista tem ciclo?", dll_without_cycle.hasCycle(
    dll_without_cycle.head))  # Output: False
