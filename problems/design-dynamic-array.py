class DynamicArray:
    
    def __init__(self, capacity: int):
        self.contents = [None for _ in range(capacity)]
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.contents[i]


    def set(self, i: int, n: int) -> None:
        self.contents[i] = n

        if i >= self.size:
            self.size = i + 1


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.contents[self.size] = n
        self.size += 1 


    def popback(self) -> int:
        value = self.contents[self.size - 1]
        self.size -= 1
        return value
 

    def resize(self) -> None:
        self.contents.extend([None for _ in range(self.capacity)])
        self.capacity *= 2


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
