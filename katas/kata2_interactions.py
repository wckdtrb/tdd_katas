import re
from logging import getLogger

def str_add(numbers):
    return_sum = 0
    return_assert = []
    numList = re.findall(r'-?\d+',numbers)

    for number in numList:
        if number[0] == '-':
            return_assert.append(number)
        elif int(number) > 1000:
            continue
        else:
            return_sum += int(number)
    if return_assert:
        getLogger("str_add").error(return_assert)
        raise AssertionError("negatives not allowed", return_assert)
    getLogger("str_add").info(return_sum)
    return return_sum