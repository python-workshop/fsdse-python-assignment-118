from linked_list import LinkedList


def partition(data, obj):
    if obj.head is None:
        return
    left = LinkedList(None)
    right = LinkedList(None)

    curr = obj.head

    # Build the left and right lists
    while curr is not None:
        if curr.data < data:
            left.append(curr.data)
        elif curr.data == data:
            right.insert_to_front(curr.data)
        else:
            right.append(curr.data)
        curr = curr.next
    curr_left = left.head
    if curr_left is None:
        return right
    else:
        # Merge the two lists
        while curr_left.next is not None:
            curr_left = curr_left.next
        curr_left.next = right.head
        return left
