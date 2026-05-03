class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        self.table[index] = [
            item for item in self.table[index]
            if item[0] != key
        ]

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"[{i}] {bucket}")

if __name__ == "__main__":
    ht = HashTable()
    ht.set("name", "Go")
    ht.set("age", 20)
    ht.set("university", "UniMelb")
    print(ht.get("name"))      
    print(ht.get("age"))         
    ht.delete("age")
    print(ht.get("age"))         
    ht.display()