
class FlatIterator:

    def __init__(self, list_of_list):
        self.incoming_list = list_of_list



    def __iter__(self):
        self.counter = 0
        self.internal_counter = 0
        return self

    def __next__(self):
        if self.counter == (len(self.incoming_list) - 1) and self.internal_counter == len(self.incoming_list):
            raise StopIteration
        else:
            length_internal_list = len(self.incoming_list[self.counter])
            if self.internal_counter < length_internal_list:
                result = (self.incoming_list[self.counter][self.internal_counter])
                self.internal_counter += 1
            else:
                self.counter += 1
                self.internal_counter = 0
                result = (self.incoming_list[self.counter][self.internal_counter])
                self.internal_counter += 1

            return result



def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()