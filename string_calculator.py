import re


class StringCalculator:
    def add(self, string: str) -> int:
        if string == "":
            return 0
        elif len(string) == 1:
            return int(string)
        else:
            numbers_list = self._process_input_string(string)

            return sum(numbers_list)

    def _process_input_string(self, string):
        numbers_list = re.split("[, \n]", string)

        if numbers_list[-1] == "":
            raise ValueError("Separators are not allowed at the end of string")

        numbers_list = [int(num) for num in numbers_list]

        return numbers_list
