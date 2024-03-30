class MyList(object):
    """List class"""

    class _ListNode(object):
        """Inner class of a list item"""

        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            """Initiate node attributes"""
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            """Return a string representation of the node"""
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Inner class of iterator"""

        def __init__(self, list_instance):
            """Initiate iterator attributes"""
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            """Return object as iterator"""
            return self

        def __next__(self):
            """Return the next item in the iterator"""
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        """List initiate"""
        self._length = 0
        self._head = None
        self._tail = None

        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Add an element to the end of the list"""
        node = MyList._ListNode(element)

        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def insert_at_index(self, index, element):
        """Insert an element at the index in the list"""
        node = MyList._ListNode(element)

        if index < 0 or index > self._length - 1:
            raise IndexError
        elif index == 0:
            current_node = self._head
            self._head = node
            self._head.next = current_node
            self._length += 1
        elif index == self._length:
            current_node = self._tail
            self._tail = node
            self._tail.next = current_node
            self._length += 1
        else:
            current_node = self._head
            for _ in range(index):
                current_node = current_node.next

            current_node.prev.next = node
            node.next = current_node
            node.prev = current_node.prev

            self._length += 1

    def remove_first(self):
        """Remove the first element from the list"""
        if self._head is None:
            return
        else:
            self._head = self._head.next
            self._length -= 1

    def remove_last(self):
        """Remove the last element from the list"""
        if self._head is None:
            return
        elif self._length == 1:
            self.remove_first()
        else:
            self._tail = self._tail.prev
            self._tail.next = None
            self._length -= 1

    def remove_at_index(self, index):
        """Remove an element at the index"""
        if index < 0 or index > self._length - 1:
            raise IndexError
        elif self._length == 1 or index == 0:
            self.remove_first()
        elif index == self._length:
            self.remove_last()
        else:
            current_node = self._head
            for _ in range(index):
                current_node = current_node.next

            current_node.prev.next = current_node.next
            self._length -= 1

    def clear(self):
        """Clear the list"""
        if self._head is None:
            return
        else:
            self._head.next = None
            self._head = self._head.next
            self._length = 0

    def __len__(self):
        """Return the length of the list"""
        return self._length

    def __repr__(self):
        """Represent the list as a string"""
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        """Get element at index"""
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        """Return an iterator"""
        return MyList._Iterator(self)


def main():
    my_list = MyList([1, 2, 3, 4, 5, 6, 7])
    print(my_list)

    try:
        my_list.insert_at_index(2, 10)
    except IndexError:
        print('Index out of range')
    print(my_list)

    my_list.remove_first()
    print(my_list)

    my_list.remove_last()
    print(my_list)

    try:
        my_list.remove_at_index(1)
    except IndexError:
        print('Index out of range')
    print(my_list)

    my_list.clear()
    print(my_list)

    print(my_list.__len__())


if __name__ == '__main__':
    main()
