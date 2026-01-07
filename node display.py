class Node:
    def __init__(self,data):
       self.data=data
       self.next=None
class sll:
    def __init__(self):
         self.head=None
    def display(self):
        temp=self.head
        if temp is None:
            print("empty linked list")
        else:
            while temp:
                print(temp.data,"->", end=" ")
                temp=temp.next
L=sll()
n1=Node(10)
L.head=n1
n2=Node(20)
L.head.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
n4.next=None
L.display()
