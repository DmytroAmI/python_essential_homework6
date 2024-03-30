class MyList:
    """MyList with revers order iterator"""
    def __init__(self, collection):
        """Initiate MyList attr"""
        self.collection = collection
        self.index = len(self.collection)

    def __iter__(self):
        """iter"""
        return self

    def __next__(self):
        """next add to the end"""
        if self.index == 0:
            raise StopIteration

        current_item = self.collection[self.index - 1]
        self.index -= 1
        return current_item

    def __str__(self):
        """Return string representation of MyList"""
        return str(self.collection)


if __name__ == '__main__':
    my_list = MyList([1, 2, 3, 4, 5])
    print(my_list)

    for item in my_list:
        print(item)
