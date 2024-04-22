

'''Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и возвращает
 их плоское представление, т. е. последовательность, состоящую из вложенных элементов. Функция test в коде ниже также
 должна отработать без ошибок.'''

class FlatIterator:

    def __init__(self, list_of_list):
        self.incoming_list = list_of_list


    def __iter__(self):
        self.counter = 0
        self.internal_counter = 0
        return self

    def __next__(self):
        if self.counter >= len(self.incoming_list):

            raise StopIteration
        else:
            # print(self.counter)
            length_internal_list = len(self.incoming_list[self.counter])
            if self.internal_counter < length_internal_list:
                result = (self.incoming_list[self.counter][self.internal_counter])
                self.internal_counter += 1
            else:

                self.internal_counter = 0
                result = (self.incoming_list[self.counter][self.internal_counter])
                self.internal_counter += 1
                self.counter += 1
            # print(result)
            return result










list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
# list_a = list(FlatIterator(list_of_lists_1))
# print(list_a)


list_2 = []
for i in FlatIterator(list_of_lists_1):
    print(i)
    # list_2.append(i)


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