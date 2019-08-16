class node:
    def __init__(self,x):
        self.data=x
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insertatbeg(self,x):
        newnode=node()
        newnode.next=head
        head=newnode
    def removeatbeg(self):
        temp=head
        head=head.next
        temp(free)
    def printlist(self):
        obj.head=node(500)
        n2=node(400)
        n3=node(300)
        n4=node(200)
        n5=node(100)
        obj.head.next=n2
        n2.next=n3
        n3.next=n4
        n4.next=n5
        temp=obj.head
        while(temp!=None):
            print(temp.data,"==>",end='')
            temp=temp.next
        print("None")    
obj=linkedlist()
ch=0
while(ch!=4):
    print("SINGLY LINKED LIST IMPLEMENTATION\n","1.insert at beg","2.delete at beg","3.print","4.exit")
    ch=int(input())
    if(ch==1):
        print("enter the value:")
        data=input()
        obj.insertatbeg(data)
        obj.printlist()
    elif(ch==2):
        obj.removeatbeg()
        obj.printlist()
    elif(ch==3):
        obj.printlist()
    else:
        print("stop the implemenatation")
        

