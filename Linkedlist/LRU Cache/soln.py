class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):


        self.capacity = capacity
        self.dict = {}
        self.head = self.tail = None

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        node.prev = node.next = None

    def add(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = self.tail = node
        node.prev = node.next = None


    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            node.val = value
            self.add(node)
        else:
            node = Node(key, value)
            self.add(node)
            self.dict[key] = node
            if len(self.dict) > self.capacity:
                node = self.tail
                self.remove(node)
                del self.dict[node.key]




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)f

if __name__ == "__main__":
    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))
    obj.put(3, 3)
    print(obj.get(3))
    obj.put(4, 4)
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))
    obj.put(5, 5)
    print(obj.get(1))
    print(obj.get(2))
    print(obj.get(3))
    print(obj.get(4))
