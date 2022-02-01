from random import *


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node) -> object:
        if self.head:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node

        else:
            self.head = new_node

    def display(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end=',')
            temp_node = temp_node.next
        print()

    def length(self):
        temp_node = self.head
        i = 0
        while temp_node:
            i = i + 1
            temp_node = temp_node.next
        return i

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


if __name__ == '__main__':
    linked_list = LinkedList()

    for i in range(10):
        linked_list.insert(Node(randint(1, 100)))

    linked_list.display()
    print("Length: "+str(linked_list.length()))