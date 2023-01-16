import re

class StringCalculator():
    def add(self, string: str) -> int:
        if string == "":
            return 0
        elif len(string) == 1:
            return int(string)
        else:
            numbers_list = re.split('[, \n]', string)
            numbers_list = [int(num) for num in numbers_list]
            return sum(numbers_list)