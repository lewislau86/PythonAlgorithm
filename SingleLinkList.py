
class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        """链表长度"""
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count


    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print(cur.item , end=" ")
            cur = cur.next


    def add(self, item):
        """头部添加元素"""
        node = SingleNode(item)
        node.next = self._head
        self._head = node



    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = SingleNode(item)

if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    print("length:",ll.length())
    ll.travel()
   # print ll.search(3)
   # print ll.search(5)
   # ll.remove(1)
   # print "length:",ll.length()
   # ll.travel()