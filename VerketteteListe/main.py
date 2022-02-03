from random import *
import Sort


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


def parition_last(start, end):
    if start == end or start is None or end is None:
        return start

    pivot_prev = start
    curr = start
    pivot = end.data

    while start != end:
        if start.data < pivot:
            pivot_prev = curr
            temp = curr.data
            curr.data = start.data
            start.data = temp
            curr = curr.next
        start = start.next

    temp = curr.data
    curr.data = pivot
    end.data = temp

    return pivot_prev


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
        k = 0
        while temp_node:
            k = k + 1
            temp_node = temp_node.next
        return k

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def find(self, j):
        place = 0
        found = False
        number_found = 0
        node = self.head
        while node:
            if j == node.data:
                print(str(j) + " befindet sich auf der Stelle " + str(place))
                found = True
                number_found += 1
            place += 1
            node = node.next
        if found:
            print(str(j) + " wurde insgesamt " + str(number_found) + " mal gefunden")
        else:
            print(str(j) + " ist nicht in der Liste")

    def quick_sort(self, start, end):
        if start is None or start == end or start == end.next:
            return

        pivot_prev = parition_last(start, end)
        self.quick_sort(start, pivot_prev)

        if pivot_prev is not None and pivot_prev == start:
            self.quick_sort(pivot_prev.next, end)

        elif pivot_prev is not None and pivot_prev.next is not None:
            self.quick_sort(pivot_prev.next.next, end)

    def min(self):
        node = self.head
        min = node.data
        while node:
            if node.data < min:
                min = node.data
            node = node.next
        print(str(min)+" ist die kleinste Zahl in der Liste")

    def max(self):
        node = self.head
        max = node.data
        while node:
            if node.data > max:
                max = node.data
            node = node.next
        print(str(max)+" ist die größte Zahl in der Liste")


if __name__ == '__main__':
    linked_list = LinkedList()

    for i in range(10):
        linked_list.insert(Node(randint(1, 100)))

    linked_list.display()
    print("Length: " + str(linked_list.length()))

    linked_list.min()
    linked_list.max()

    n = linked_list.head
    while n.next is not None:
        n = n.next

    linked_list.quick_sort(linked_list.head, n)
    linked_list.display()
