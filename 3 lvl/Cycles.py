# 34722988
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


def hasCycle(head):
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next

        if slow == fast:
            return True

    return False
