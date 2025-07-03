# basic_data_structures.py
# Arrays and Matrices
class CustomArray:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def delete(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]

    def access(self, index):
        return self.data[index] if 0 <= index < len(self.data) else None

# Stack using array
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def peek(self):
        return self.stack[-1] if self.stack else None

# Queue using array
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

# Singly Linked List
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def delete(self, val):
        current = self.head
        prev = None
        while current:
            if current.val == val:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def traverse(self):
        values = []
        current = self.head
        while current:
            values.append(current.val)
            current = current.next
        return values

# Demo and Output 
if __name__ == "__main__":
    print("Testing Basic Data Structures:\n")

    # Array
    arr = CustomArray()
    arr.insert(5)
    arr.insert(10)
    print("Array contents:", arr.data)
    arr.delete(0)
    print("Array after deletion:", arr.data)

    # Stack
    stk = Stack()
    stk.push(1)
    stk.push(2)
    print("Stack peek:", stk.peek())
    stk.pop()
    print("Stack after pop:", stk.stack)

    # Queue
    q = Queue()
    q.enqueue('A')
    q.enqueue('B')
    print("Queue dequeue:", q.dequeue())
    print("Queue after dequeue:", q.queue)

    # Linked List
    ll = SinglyLinkedList()
    ll.insert(100)
    ll.insert(200)
    ll.insert(300)
    print("Linked List traversal:", ll.traverse())
    ll.delete(200)
    print("Linked List after deletion:", ll.traverse())
