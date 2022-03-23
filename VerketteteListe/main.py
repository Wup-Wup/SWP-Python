import random
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.data


def swapData(first, second):
    value = first.data
    first.data = second.data
    second.data = value


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
            k += 1
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
                    node.prev.next = node
                    break
                node.prev = None
            node = node.next
        if not found:
            print(str(before) + " ist nicht in der Liste")

    def sortASC(self):
        front = self.head
        back = None
        while front is not None:
            back = front.next
            while back is not None and back.prev is not None and back.data < back.prev.data:
                swapData(back, back.prev)
                back = back.prev
            front = front.next

    def sortDESC(self):
        front = self.head
        back = None
        while front is not None:
            back = front.next
            while back is not None and back.prev is not None and back.data > back.prev.data:
                swapData(back, back.prev)
                back = back.prev
            front = front.next


class ArrayList:

    def __init__(self):
        self.list = []

    def insert(self, data):
        self.list.append(data)

    def delete_at_index(self, index):
        self.list.pop(index)

    def delete_after(self, index):
        if len(self.list) > index + 1:
            self.list.pop(index + 1)

    def delete_before(self, index):
        if index - 1 >= 0:
            self.list.pop(index - 1)

    def insert_at_index(self, index, newD):
        self.list.insert(index, newD)

    def insert_after(self, index, newD):
        self.list.insert(index + 1, newD)

    def insert_before(self, index, newD):
        if index - 1 >= 0:
            self.list.insert(index - 1, newD)

    def display(self):
        for i in self.list:
            print(i, end=',')

    def returnAllDesc(self):
        for i in reversed(self.list):
            print(i)

    def length(self):
        return len(self.list)

    def sortASC(self):
        for i in range(1, self.length()):
            key = self.list[i]
            j = i - 1
            while j >= 0 and key < self.list[j]:
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j+1] = key

    def sortDESC(self):
        for i in range(1, self.length()):
            key = self.list[i]
            j = i - 1
            while j >= 0 and key > self.list[j]:
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j + 1] = key


if __name__ == '__main__':

    linked_list = LinkedList()
    array_list = ArrayList()

    for i in range(10000):
        x = random.randint(0, 1000)
        linked_list.insert(Node(x))
        array_list.insert(x)

    start = time.time()
    linked_list.sortASC()
    print("Das Sortieren der Linkedlist dauerte: ")
    print('{:5.3f}s'.format(time.time() - start))
    print()

    start = time.time()
    array_list.sortASC()
    print("Das Sortieren der Arraylist dauerte: ")
    print('{:5.3f}s'.format(time.time() - start))
    print()
