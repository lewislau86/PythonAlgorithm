import random
import sys

from line_profiler import LineProfiler
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
        print("\n")


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

    def get(self, pos):
        """获取指定位置的元素"""
        if pos <= 0:
            return self._head
        cur = self._head
        count = 0
        while count < pos:
            count += 1
            cur = cur.next
        return cur

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = SingleNode(item)
            cur = self.get(pos - 1)
            node.next = cur.next
            cur.next = node

    def remove(self, pos):
        """删除节点"""
        if pos <= 0:
            self._head = self._head.next
        elif pos > (self.length() - 1):
            pass
        else:
            cur = self.get(pos - 1)
            cur.next = cur.next.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
    ''' 
    单链表反转有两种办法
    1. 递归
    2. 非递归
    '''
    def reverse2(self):
        """反转链表 非递归"""
        cur = self._head
        pre = None
        while cur != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        self._head = pre

    def reverse1(self):
        """反转链表 递归"""
        self._reverse(self._head)

    def _reverse(self, head):
        """反转链表 递归"""
        if head==None or head.next == None :
            return head
        else:
            new_head = self._reverse(head.next)
            head.next.next = head
            head.next = None
            return new_head

    def sort(self):
        """排序"""
        if self.is_empty():
            return
        self._sort(self._head)

    def _sort(self, head):
        pass
        """排序
        if head==None or head.next == None:
            return head
        else:
            cur = head
            while cur.next != None:
                if cur.item > cur.next.item:
                    cur.item, cur.next.item = cur.next.item, cur.item
                cur = cur.next
            self._sort(head)
        """




if __name__ == "__main__":
    ll = SingleLinkList()
    lp = LineProfiler()
    #lp_wrapper = lp(ll.add)
    #lp_wrapper(1)
    #lp.print_stats()
    #ll.add(1)
    for i in range(10):
        ll.add(random.randint(0,1000))
    #ll.travel()
    ll.sort()
    ll.travel()

'''
    lp.add_function(ll.reverse2)
    lp.add_function(ll.reverse1)
    lp.enable()
    ll.reverse1()
    ll.reverse2()
    lp.disable()
    lp.print_stats(sys.stdout)
   
   '''

   # print ll.search(3)
   # print ll.search(5)
   # ll.remove(1)
   # print "length:",ll.length()
   # ll.travel()