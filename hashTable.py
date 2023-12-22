class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for pair in self.table[index]:
                if pair[0] == key:
                    # Update value if key already exists
                    pair = (key, value)
                    return
            # Append new key-value pair if key doesn't exist
            self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index] or []:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index] or []):
            if pair[0] == key:
                del self.table[index][i]
                return
        raise KeyError(f"Key '{key}' not found")

# Example usage:
my_table = HashTable(size=10)
my_table.insert("name", "John")
my_table.insert("age", 25)
my_table.insert("city", "New York")

print("Get 'name':", my_table.get("name"))
print("Get 'age':", my_table.get("age"))

# Update value
my_table.insert("age", 26)
print("Updated 'age':", my_table.get("age"))

# Remove key
my_table.remove("city")
try:
    print("Get 'city':", my_table.get("city"))
except KeyError as e:
    print(e)
