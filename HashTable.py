class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash(self, key):
        # La función hash toma una clave y devuelve un índice calculado
        # utilizando una función hash.
        return hash(key) % self.size

    def insert(self, key, value):
        # El método insert toma una clave y un valor,
        # y los almacena en la hash table.
        index = self.hash(key)
        self.buckets[index].append((key, value))

    def get(self, key):
        # El método get toma una clave
        # y devuelve el valor correspondiente almacenado en la hash table.
        index = self.hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        # El método remove toma una clave
        #  y elimina el par clave-valor correspondiente de la hash table.
        index = self.hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]
                return

    def retrieve_all(self):
        # El método retrieve_all devuelve todos
        # los valores almacenados en la hash table.
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket:
                all_values.append(value)
        return all_values
