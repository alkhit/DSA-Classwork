class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBeginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
            last.next = new_node

    def deleteBeginning(self):
        if self.head is None:
            return "The list is empty"
        self.head = self.head.next
    
    def deleteEnd(self):
        if self.head is None:
            return "Empty list"
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.text = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertBeginning("Fox")
    ll.insertBeginning("Brown")
    ll.insertBeginning("The")
    ll.printList()

    ll.insertEnd("Is Sleeping")
    ll.printList()

    ll.deleteEnd()
    ll.printList()

    ll.deleteBeginning()
    ll.printList()

    ll.insertBeginning("A")
    ll..printList()