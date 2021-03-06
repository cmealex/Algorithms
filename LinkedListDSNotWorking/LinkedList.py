from LinkedListDSNotWorking.Node import Node


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.counter = 0

    def insertStart(self, data):
        newNode = Node(data)
        self.counter += 1

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def size(self):
        return self.counter

    def insertEnd(self, data):
        newNode = Node(data)
        actualNode = self.head
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def remove(self, data):

        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode
            else:
                self.head.remove()

    def traverseList(self):
        actualNode = self.head
        while actualNode.nextNode is not None:
            print actualNode.data
            actualNode = actualNode.nextNode

