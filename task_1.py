

'''Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и возвращает
 их плоское представление, т. е. последовательность, состоящую из вложенных элементов. Функция test в коде ниже также
 должна отработать без ошибок.'''

class FlatIterator:

    def __init__(self, list_of_list):
        self.input_list = list_of_list
        self.result = []

    def __iter__(self):
        self.counter = 0

        return self

    def __next__(self):
        if self.counter < len(self.input_list):
            item = self.input_list[self.counter]
            self.counter += 1
            self.result.extend(item)
            # print(self.result)
            return item
        else:
            raise StopIteration


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

for i in FlatIterator(list_of_lists_1):
    print(i)

#['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]




# def test_1():
#
#     list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
#
#     for flat_iterator_item, check_item in zip(
#             FlatIterator(list_of_lists_1),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     ):
#
#         assert flat_iterator_item == check_item
#
#     assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#
#
# if __name__ == '__main__':
#     test_1()