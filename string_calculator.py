class StringCalculator():
    def add(self, string: str) -> int:
        if string == "":
            return 0
        elif len(string) == 1:
            return int(string)
        else:
            number1, number2 = string.split(",")
            return int(number1) + int(number2)