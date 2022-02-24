from random import *


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if self.head:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            new_node.prev = last_node
            last_node.next = new_node

        else:
            self.head = new_node

    def display(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end=',')
            temp_node = temp_node.next
        print('')

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
                print(str(j) + " befindet sich auf der Stelle " + str(place) +" (startet mit 0)")
                found = True
                number_found += 1
            place += 1
            node = node.next
        if found:
            print(str(j) + " wurde insgesamt " + str(number_found) + " mal gefunden")
        else:
            print(str(j) + " ist nicht in der Liste")

    def min(self):
        node = self.head
        min = node.data
        while node:
            if node.data < min:
                min = node.data
            node = node.next
        print(str(min) + " ist die kleinste Zahl in der Liste")

    def max(self):
        node = self.head
        max = node.data
        while node:
            if node.data > max:
                max = node.data
            node = node.next
        print(str(max) + " ist die größte Zahl in der Liste")

    def sort_asc(self):
        head = self.head
        current = head
        while current.next is not None:
            if current.next.data > current.data:
                current = current.next
            else:
                temp = current.next
                current.next = temp.next
                if head.data > temp.data:
                    temp.next = head
                    self.head = temp
                    head = self.head
                else:
                    inpos = head
                    while temp.data > inpos.next.data:
                        inpos = inpos.next
                    temp.next = inpos.next
                    inpos.next = temp

    def sort_desc(self):
        head = self.head
        node = self.head
        while node.next is not None:
            if node.next.data < node.data:
                node = node.next
            else:
                temp = node.next
                node.next = temp.next
                if head.data < temp.data:
                    temp.next = head
                    self.head = temp
                    head = self.head
                else:
                    inpos = head
                    while temp.data < inpos.next.data:
                        inpos = inpos.next
                    temp.next = inpos.next
                    inpos.next = temp

    def insert_after(self,value,after):
        found = False
        node = self.head
        while node:
            if after == node.data:
                found = True
                temp_prev = node
                temp_next = node.next
                node.next = value
                node = node.next
                node.prev = temp_prev
                node.next = temp_next
                node = node.next
                node.prev = value
                break
            node = node.next
        if not found:
            print(str(after) + " ist nicht in der Liste")

    def insert_before(self, value, before):
        found = False
        node = self.head
        while node:
            if before == node.data:
                found = True
                temp_next = node
                temp_prev = node.prev
                node.prev = value
                node = node.prev
                node.next = temp_next
                node.prev = temp_prev
                node = node.prev
                node.next = value
                break
            node = node.next
        if not found:
            print(str(before) + " ist nicht in der Liste")

    def delete_after(self, after):
        found = False
        node = self.head
        while node:
            if after == node.data:
                found = True
                if node.next is None:
                    print(str(after) + " ist schon das letzte Element")
                    break
                if node.next.next is not None:
                    node.next = node.next.next
                    node.next.next.prev = node
                    break
                node.next = None
            node = node.next
        if not found:
            print(str(after) + " ist nicht in der Liste")

    def delete_before(self, before):
        found = False
        node = self.head
        while node:
            if before == node.data:
                found = True
                if node.prev is None:
                    print(str(before) + " ist schon das erste Element")
                    break
                if node.prev.prev is not None:
                    node.prev = node.prev.prev
                    node.prev.prev.next = node
                    break
                node.prev = None
            node = node.next
        if not found:
            print(str(before) + " ist nicht in der Liste")


if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.insert(Node(2))
    linked_list.insert(Node(8))
    linked_list.insert(Node(5))
    linked_list.insert(Node(8))

    linked_list.display()
    print("Length: " + str(linked_list.length()))

    #linked_list.min()
    #linked_list.max()

    linked_list.insert_after(Node(12),8)
    linked_list.display()
    linked_list.insert_before(Node(14),12)
    linked_list.display()

    linked_list.insert(Node(31))
    linked_list.insert(Node(74))
    linked_list.insert_before(Node(99),31)
    #linked_list.find(99)
    linked_list.display()
    linked_list.delete_after(31)
    linked_list.delete_before(12)
    linked_list.display()
