class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def count_nodes(self):
        c=0
        temp=self.head
        while temp:
            c=c+1
            temp=temp.next
        print(c)
    def display(self):
        if self.head is None:
            print("EMpty linked list")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
L=SLL()
n1=Node(10)
L.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
L.display()
print()
L.count_nodes()
