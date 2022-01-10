
# Online Python - IDE, Editor, Compiler, Interpreter

def list_concat(lists):
    """
    Joins given list of lists into a single list
    """
    final_list = []
    for sublist in lists:
        final_list.extend(sublist)
    return final_list

a = [[1,2,3], [4,5,6], [7,8,9], [10]]
print(list_concat(a))

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
