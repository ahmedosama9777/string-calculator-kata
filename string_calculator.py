import re


class StringCalculator:
    DELIMETER = ""

    def add(self, string: str) -> int:
        if string == "":
            return 0
        elif len(string) == 1:
            return int(string)
        else:
            numbers_list = self._process_input_string(string)

            return sum(numbers_list)

    def _process_input_string(self, string: str):
        if string.startswith("//"):
            self.DELIMETER = re.split("[// \n]", string)[2]

        if not string[-1].isnumeric():
            raise ValueError("Separators are not allowed at the end of string")

        string = re.sub(f"[// {self.DELIMETER} , \n]", "", string)
        numbers_list = list(string)

        numbers_list = [int(num) for num in numbers_list]

        return numbers_list
