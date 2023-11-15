import unittest

############################################################################################
def date_to_tuple(date_str):
    year, month, day = date_str.split('-')
    return (day, month, year)

class TestDateConversion(unittest.TestCase):
    def test_date_to_tuple(self):
        self.assertEqual(date_to_tuple('2025-12-31'), ('31', '12', '2025'))
        self.assertEqual(date_to_tuple('2023-05-15'), ('15', '05', '2023'))

if __name__ == '__main__':
    unittest.main()
############################################################################################
def sum_of_list_elements(lst):
    return sum(int(x) for x in lst)

class TestSumOfListElements(unittest.TestCase):
    def test_sum_of_list_elements(self):
        self.assertEqual(sum_of_list_elements(['1', '2', '3', '4', '5']), 15)
        self.assertEqual(sum_of_list_elements(['10', '20', '30']), 60)
        self.assertEqual(sum_of_list_elements(['-1', '0', '1']), 0)
        self.assertEqual(sum_of_list_elements([]), 0)

if __name__ == '__main__':
    unittest.main()
############################################################################################

def divide_first_half_by_second_half(lst):
    if len(lst) % 2 != 0:
        raise ValueError("Список должен иметь четное количество элементов")
    
    midpoint = len(lst) // 2
    first_half_sum = sum(lst[:midpoint])
    second_half_sum = sum(lst[midpoint:])
    
    if second_half_sum == 0:
        raise ValueError("Сумма второй половины элементов равна нулю")
    
    return first_half_sum / second_half_sum

class TestDivideFirstHalfBySecondHalf(unittest.TestCase):
    def test_divide_first_half_by_second_half(self):
        self.assertAlmostEqual(divide_first_half_by_second_half([1, 2, 3, 4, 5, 6]), 0.6, places=2)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            divide_first_half_by_second_half([])

    def test_odd_length_list(self):
        with self.assertRaises(ValueError):
            divide_first_half_by_second_half([1, 2, 3, 4, 5])

    def test_zero_in_second_half(self):
        with self.assertRaises(ValueError):
            divide_first_half_by_second_half([1, 2, 3, 0, 5, 6])

if __name__ == '__main__':
    unittest.main()
############################################################################################
def merge_dicts(dct1, dct2):
    result = dct1.copy()
    result.update(dct2)
    return result

class TestMergeDicts(unittest.TestCase):
    def test_merge_dicts(self):
        dct1 = {'a': 1, 'b': 2}
        dct2 = {'c': 3, 'd': 4}
        expected_result = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        
        merged_dict = merge_dicts(dct1, dct2)
        self.assertEqual(merged_dict, expected_result)

if __name__ == '__main__':
    unittest.main()
############################################################################################
def sum_dict_elements(dct):
    total_sum = 0
    for outer_key, inner_dict in dct.items():
        for inner_key, value in inner_dict.items():
            total_sum += value
    return total_sum

class TestSumDictElements(unittest.TestCase):

    def test_sum_dict_elements(self):
        dct = {
            1: {
                1: 11,
                2: 12,
                3: 13,
            },
            2: {
                1: 21,
                2: 22,
                3: 23,
            },
            3: {
                1: 24,
                2: 25,
                3: 26,
            }
        }
        self.assertEqual(sum_dict_elements(dct), 195)

if __name__ == '__main__':
    unittest.main()

