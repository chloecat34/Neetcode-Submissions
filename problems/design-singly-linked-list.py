# Helper function because LinkedList doesn't have arguments
def make_list(head, link) -> LinkedList:
    ls = LinkedList()
    ls.head = head
    ls.link = link
    return ls

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.link = None

    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        elif index == 0:
            return self.head
        elif self.link is None:
            return -1
        else:
            return self.link.get(index - 1)
        

    def insertHead(self, val: int) -> None:
        if self.head is not None:
            self.link = make_list(self.head, self.link)

        self.head = val
        

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = val
        elif self.link is None:
            self.link = make_list(val, None)
        else:
            self.link.insertTail(val)
        

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        elif index == 0:
            if self.link is None:
                self.head = None
            else:
                self.head = self.link.head
                self.link = self.link.link

            return True
        elif self.link is None:
            return False
        else:
            return self.link.remove(index - 1)
        

    def getValues(self) -> List[int]:
        values = []

        current = self

        while not (current is None or current.head is None):
            values.append(current.head)
            current = current.link

        return values
        
