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
    def insert(self,index,data):
        n=node(data)
        temp=self.head
        if self.head!=None:
                for i in range(index):
                    if temp.next==None:
                        self.append(data)
                        return None
                    temp=temp.next
                if index==0:
                        self.head.back=n
                        n.next=self.head
                        self.head=n
                else:
                    print(temp.data)
                    n.next=temp
                    n.back=temp.back
                    temp.back.next=n
                    temp.back=n
        else:
            self.append(data)
    def display(self):
        if self.head==None:
            print("This DL list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end="")
                temp=temp.next
    def display_reverse(self):
        if self.head==None:
            print("This DL list is empty")
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            while temp:
                print(temp.data,"<-->",end="")
                temp=temp.back
    def copy(self):
      list=DLL()
      temp=self.head
      while temp:
          list.append(temp.data)
          temp=temp.next
      return list             
    def count(self):
          temp=self.head
          len=0
          while temp:
            temp=temp.next
            len=len+1
          return len  
    def remove(self,data):
        temp=self.head
        while temp:
            if temp.data==data:
                if temp==self.head:
                    return self.popstart()
                elif temp.next==None:
                    temp2=temp.back
                    temp.back=None
                    temp2.next=None
                    return temp.data
                else:
                    temp.next.back=temp.back
                    temp.back.next=temp.next
                    return temp.data
            temp=temp.next
        return None
    def pop(self,index):
        temp=self.head
        if self.head==None:
          return None
        for i in range(index):
          temp=temp.next
          if temp==None:
              return None
        if temp==self.head:
            return self.popstart()
        elif temp.next==None:
            temp2=temp.back
            temp.back=None
            temp2.next=None
            return temp.data
        else:
            temp.next.back=temp.back
            temp.back.next=temp.next
            return temp.data
    def popend(self):
        if self.head==None:
            return None
        elif self.head.next==None:
            poped_node=self.head
            
            self.head=None
            
            return poped_node.data
        else:    
            temp=self.head
            
            while temp.next.next:
                temp=temp.next
            poped_node=temp.next
            
            temp.next=None
            return poped_node.data
    def popstart(self):
        if self.head==None:
            return None
        elif self.head.next==None:
            poped_node=self.head
            
            self.head=None
            
            return poped_node.data
        else:
            temp=self.head
            poped_node=temp
            
            self.head=temp.next
            temp.next.back=None
            return poped_node.data
    def index(self,data):
        temp=self.head
        result=False
        index=0
        while temp:
            if temp.data==data:
                result=True
                break
            temp=temp.next
            index=index+1
        if result==True:
            return index
        else:
            return None
    def value(self,index):
      temp=self.head
      if self.head==None:
          return None
      for i in range(index):
          if temp.next==None:
              return None
          temp=temp.next
      return temp.data
    def clear(self):
        while self.head!=None:
            if self.head.next==None:
                self.head=None
            else:
                temp=self.head
                self.head=temp.next
                temp.next.back=None
    def sum_of_maxsubscript(self):
        c=0
        m=0
        temp=self.head
        while temp:
            a=temp.data+c
            c=max(temp.data,a)
            m=max(m,c)
            temp=temp.next
        return m
l1=DLL()
l1.append(5)
l1.append(-4)
l1.append(5)
l1.append(6)
l1.append(-10)
l1.append(15)
l1.display()
print("\n")

print(l1.sum_of_maxsubscript())

