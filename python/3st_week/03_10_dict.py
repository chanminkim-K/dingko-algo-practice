class LinkedTuple:
    def __init__(self):
        self.item = []

    def add(self, key, value):
        self.item.append((key, value))

    def get(self, key):
        for k, v in self.item:
            if k == key:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)


class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("1", 1)
my_dict.put("2", 2)
my_dict.put("3", 3)
my_dict.put("4", 4)
my_dict.put("5", 5)
my_dict.put("6", 6)
my_dict.put("7", 7)
my_dict.put("8", 8)
my_dict.put("9", 9)
print(my_dict.items)
print("충돌 해결 전 ", my_dict.get("1"))


my_dict2 = LinkedDict()
my_dict2.put("1", 1)
my_dict2.put("2", 2)
my_dict2.put("3", 3)
my_dict2.put("4", 4)
my_dict2.put("5", 5)
my_dict2.put("6", 6)
my_dict2.put("7", 7)
my_dict2.put("8", 8)
my_dict2.put("9", 9)
print("충돌 해결 후 ", my_dict2.get("1"))  # 3이 반환되어야 합니다!