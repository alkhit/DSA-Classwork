class LinkedList:
    def __init__ (self,value,nextNode = None):
        self.value = value
        self.nextNode = nextNode

snode1 = LinkedList("1")
snode2 = LinkedList("2")
snode3 = LinkedList("3")
snode4 = LinkedList("4")

snode1.nextNode = snode2
snode2.nextNode = snode3
snode3.nextNode = snode4

currentNode = snode1

while True:
    print(currentNode.value, ">>", end=" ")
    if currentNode.nextNode is None:
        print("None")
        break

    currentNode = currentNode.nextNode