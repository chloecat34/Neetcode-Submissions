class LinkNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1

        dummy = self.head

        while dummy is not None:
            if index == 0:
                return dummy.value

            dummy = dummy.next
            index -= 1


        return -1
        

    def insertHead(self, val: int) -> None:
        node = LinkNode(val)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        

    def insertTail(self, val: int) -> None:
        node = LinkNode(val)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            # The old tail must connect to the new one
            self.tail.next = node
            self.tail = node
        

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        # special case for the first value
        if index == 0:
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            return True

        dummy = self.head

        while not (dummy is None or dummy.next is None):
            index -= 1

            if index == 0:
                # delete the next value
                dummy.next = dummy.next.next

                if dummy.next is None:
                    self.tail = dummy

                return True

            dummy = dummy.next

        return False
        

    def getValues(self) -> List[int]:
        values = []

        dummy = self.head

        while dummy is not None:
            values.append(dummy.value)
            dummy = dummy.next

        return values
        
