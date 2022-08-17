class node:
    def __init__(self,data,next=None,back=None):
        self.data=data
        self.next=next
        self.back=back

class DLL:
    def __init__(self):
        self.head=None
    def append(self,data):
        n=node(data)
        if self.head==None:
            self.head=n
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=n
            n.back=temp
    def display(self):
        if self.head==None:
            print("This DL list is empty")
        else:
            temp=self.head
            for i in range(self.count()):
                print(temp.data,"<-->",end="")
                temp=temp.next
    def count(self):
          temp=self.head
          len=0
          while temp:
            temp=temp.next
            len=len+1
          return len  
l1=DLL()
l1.append(5)
l1.append(10)
l1.append(15)
l1.append(20)
l1.append(25)
l1.append(30)
l1.append(35)
l1.append(40)

l1.display()
print(l1.count())
