class Node:

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        next_node = node.next
        prev_node = node.prev

        node.next.prev = prev_node
        node.prev.next = next_node

    def add(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

        

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val
        
        

    def put(self, key: int, val: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.val = val
            self.remove(node)
            self.add(node)
            return

        if len(self.cache) == self.capacity:
            lru = self.tail.prev
            
            self.remove(lru)
            del self.cache[lru.key]
        
        new_node = Node(key, val)
        self.add(new_node)
        self.cache[key] = new_node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
