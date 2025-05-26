import os
import sys
# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from linked_lists.linked_list import Node
from linked_lists.linked_list import DoublyLinkedList


class Solution:
    def middleNode(self, head: Node) -> Node:
        ahead = head

        while ahead and ahead.next:
            ahead = ahead.next.next

            head = head.next
        return head


# testes manuais
if __name__ == "__main__":

    dll = DoublyLinkedList()

    dll.add_to_end(1)
    dll.add_to_end(2)
    dll.add_to_end(3)
    dll.add_to_end(4)
    dll.add_to_end(5)

    print("Lista original:")
    dll.print_list()

    sol = Solution()
    middle_node = sol.middleNode(dll.head)

    print("Nó do meio:", middle_node.value if middle_node else "Nenhum nó")

    # outra lista de teste
    dll2 = DoublyLinkedList()
    dll2.add_to_end(1)
    dll2.add_to_end(2)
    dll2.add_to_end(3)
    dll2.add_to_end(4)
    dll2.add_to_end(5)
    dll2.add_to_end(6)
    print("\nOutra lista original:")
    dll2.print_list()
    middle_node2 = sol.middleNode(dll2.head)
    print("Nó do meio:", middle_node2.value if middle_node2 else "Nenhum nó")
