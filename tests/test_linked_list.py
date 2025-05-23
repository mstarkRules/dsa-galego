import os
import sys
# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.reverse_linked_list import ListNode, Solution


def list_to_linkedlist(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head


def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def test_reverse_empty_list():
    print("\nTest: Lista vazia")
    sol = Solution()
    head = None
    reversed_head = sol.reverseList(head)
    print("Resultado:", linkedlist_to_list(reversed_head))
    assert reversed_head is None


def test_reverse_single_element():
    print("\nTest: Um elemento")
    sol = Solution()
    head = ListNode(1)
    reversed_head = sol.reverseList(head)
    print("Resultado:", linkedlist_to_list(reversed_head))
    assert linkedlist_to_list(reversed_head) == [1]


def test_reverse_multiple_elements():
    print("\nTest: Vários elementos")
    sol = Solution()
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    print("Original:", linkedlist_to_list(head))
    reversed_head = sol.reverseList(head)
    print("Reverso:", linkedlist_to_list(reversed_head))
    assert linkedlist_to_list(reversed_head) == [5, 4, 3, 2, 1]
