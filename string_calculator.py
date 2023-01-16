class StringCalculator():
    def add(self, string: str) -> int:
        if string == "":
            return 0
        elif len(string) == 1:
            return int(string)
        else:
            numbers_list = string.split(",")
            numbers_list = [int(num) for num in numbers_list]
            return sum(numbers_list)