class LinkedQueue:
    "fifo "
    class _Node:
        slots =' _element' ,  ' _next'

    def __init__(self) -> None:
        self._head=None
        self._tail=None
        self._size=0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size==0
    
    def first(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self._head._element
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('stack is empty')
        answer=self._head._element
        self._head=self.head._next
        self._size-=1
        if self.is_empty():
            self._tail=None
        return answer
    
    def engueue(self,e):
        newest=self._Node(e,None)
        if self.is_empty():
            self._head=newest
        else:
            self._tail._next=newest
            self._tail=newest
            self._size+=1
