class Node():
    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def set_next(self, nxt):
        self._next = nxt

    def get_next(self):
        return self._next

    def set_prev(self, prev):
        self._prev = prev

    def get_prev(self):
        return self._prev


class DoubleLinkedList():
    def __init__(self):
        self._head = None

    def __iter__(self):
        node = self._head

        while node:
            yield node
            node = node.get_next()

    def __len__(self):
        _len = 0
        for node in self.__iter__():
            _len += 1
        return _len

    def __contains__(self, data):
        for node in self.__iter__():
            if node.get_data() == data:
                return True
        return False

    def push_tail(self, data):
        new_node = Node(data)
        for node in self:
            next_node = node.get_next()
            if (next_node is None):
                node.set_next(new_node)
                new_node.set_prev(node)
                break

        if self._head == None:
            self._head = new_node

    def push_head(self, data):
        new_node = Node(data)
        node = self._head

        new_node.set_next(node)
        node.set_prev(new_node)
        self._head = new_node

    def pop_head(self):
        node = self._head
        next_node = node.get_next()
        next_node.set_prev(None)
        self._head = next_node

    def pop_tail(self):
        for node in self:
            next_node = node.get_next()
            prev_node = node.get_prev()
            if next_node is None:
                prev_node.set_next(None)
                break

    def remove(self, remove_data):
        for node in self:
            next_node = node.get_next()
            prev_node = node.get_prev()
            if node.get_data() == remove_data:
                if node == self._head:
                    self._head = next_node
                    next_node.set_prev(None)
                else:
                    prev_node.set_next(next_node)
                    next_node.set_prev(prev_node)

    def insert_before(self, find_data, insert_data):

        for node in self:
            prev_node = node.get_prev()
            if node.get_data() == find_data:
                new_node = Node(insert_data)
                new_node.set_next(node)
                if node.get_data() == self._head.get_data():
                    self._head = new_node
                    new_node.set_prev(None)
                else:
                    prev_node.set_next(new_node)
                    new_node.set_prev(prev_node)
                break

    def insert_after(self, find_data, insert_data):
        for node in self:
            next_node = node.get_next()
            if node.get_data() == find_data:
                new_node = Node(insert_data)
                node.set_next(new_node)
                new_node.set_next(next_node)
                new_node.set_prev(node)
                break

    def __str__(self):
        mystring = []
        for node in self:
            mystring.append(node.get_data())
        return " -> ".join(mystring)


STRINGS = ["Donald", "John", "Trump"]

my_list = DoubleLinkedList()

for data in STRINGS:
    my_list.push_tail(data)

print(my_list)

print("Removing last item from linked list...\n")
my_list.pop_tail()
print(my_list)

print("Adding (" + STRINGS[2] + ") to last item in linked list...\n")
my_list.push_tail(STRINGS[2])
print(my_list)

print("Removing (" + STRINGS[1] + ") from the linked list...\n")
my_list.remove(STRINGS[1])
print(my_list)

print("Inserting (" + STRINGS[1] + ") BEFORE (" + STRINGS[2] + ") in the linked list...\n")
my_list.insert_before(STRINGS[2], STRINGS[1])
print(my_list)

print("Removing the first item from the linked list...\n")
my_list.pop_head()
print(my_list)

print("Inserting (" + STRINGS[0] + ") at the head of the linked list...\n")
my_list.push_head(STRINGS[0])
print(my_list)

print("Inserting " + "(loses)" + " AFTER (" + STRINGS[2] + ") in the linked list...\n")
my_list.insert_after(STRINGS[2], "loses")
print(my_list)

print("Searching for (" + STRINGS[2] + ") in the linked list...\n")
if STRINGS[2] in my_list:
    print("FOUND.")
else:
    print("NOT FOUND.")

print("The length of this linked list is...\n")
print(len(my_list))

for node in my_list:

    print("Node: " + node.get_data())

    if node.get_prev():
        print("Prev: " + node.get_prev().get_data())
    else:
        print("Prev: None")

    if node.get_next():
        print("Next: " + node.get_next().get_data())
    else:
        print("Next: None")

    print("\n")