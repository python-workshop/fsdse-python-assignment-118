from unittest import TestCase
from linked_list import LinkedList, Node

class TestPartition(TestCase):
    def test_partition(self):
        try:
            from build import partition
        except ImportError:
            self.assertFalse("no function found")


        linked_list = LinkedList(None)
        partition(10, linked_list)
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: One element list, left list empty')
        linked_list = LinkedList(Node(5))
        partition(0, linked_list)
        self.assertEqual(linked_list.get_all_data(), [5])

        print('Test: Right list is empty')
        linked_list = LinkedList(Node(5))
        partition(10, linked_list)
        self.assertEqual(linked_list.get_all_data(), [5])

        print('Test: General case')
        # Partition = 10
        # Input: 4, 3, 13, 8, 10, 1, 14, 10, 12
        # Output: 4, 3, 8, 1, 10, 10, 13, 14, 12
        linked_list = LinkedList(Node(12))
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(14)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(8)
        linked_list.insert_to_front(13)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(4)
        partitioned_list = partition(10, linked_list)
        self.assertEqual(partitioned_list.get_all_data(),
                     [4, 3, 8, 1, 10, 10, 13, 14, 12])
