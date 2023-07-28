class ContactList:
    def __init__(self, size):
        self._contacts = [[] for _ in range(size)]
        self._size = size

    def _hash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self._size

    def insert(self, name, phone):
        index = self._hash(name)
        if self._contacts[index] is None:
            self._contacts[index] = []
        for i, contact in enumerate(self._contacts[index]):
            if contact[0] == name:
                self._contacts[index][i] = [name, phone]
                return
        self._contacts[index].append([name, phone])

    def get(self, name):
        index = self._hash(name)
        if self._contacts[index] is not None:
            for contact in self._contacts[index]:
                if contact[0] == name:
                    return contact[1]
        return None

    def retrieveAll(self):
        all_contacts = []
        for bucket in self._contacts:
            if bucket is not None:
                all_contacts.extend(bucket)
        return all_contacts

    def delete(self, name):
        index = self._hash(name)
        if self._contacts[index] is not None:
            for i, contact in enumerate(self._contacts[index]):
                if contact[0] == name:
                    del self._contacts[index][i]
                    return
        return None
