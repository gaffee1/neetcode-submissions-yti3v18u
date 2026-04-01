class MyHashMap:

    def __init__(self):
        self.data = {}

    def put(self, key: int, value: int) -> None:
        self.data.update({key : value})

    def get(self, key: int) -> int:
        if key in self.data:
            return self.data[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.pop(key)
