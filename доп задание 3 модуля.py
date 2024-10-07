
def data_sum(data_structure):
    number = 0
    for i in data_structure:
        if isinstance(i, int): #если число
            number+=i
        elif isinstance(i,str):
            number += len(i)
        elif isinstance(i,list):
            number += data_sum(i)
        elif isinstance(i,tuple):
            for element in i:
                if isinstance(element, int):
                    number += element
                elif isinstance(element, dict):
                    for key, value in element.items():
                        number += len(key)
                        number += value
                elif isinstance(element, list):
                    for item in element:
                        if isinstance(item, set):
                            for inner_tuple in item:
                                if isinstance(inner_tuple, tuple):
                                    for sub_element in inner_tuple:
                                        if isinstance(sub_element, int):
                                            number += sub_element
                                        elif isinstance(sub_element, str):
                                            number += len(sub_element)
                                        elif isinstance(sub_element, tuple):
                                            for sub_sub_element in sub_element:
                                                if isinstance(sub_sub_element, int):
                                                    number += sub_sub_element
                                                elif isinstance(sub_sub_element, str):
                                                    number += len(sub_sub_element)

        elif isinstance(i, dict):
            sum_k = sum(len(key) for key in i)
            sum_v = sum(i.values())
            result = sum_k + sum_v
            number += result
    return number

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum_data_str = data_sum(data_structure)
print(sum_data_str)
