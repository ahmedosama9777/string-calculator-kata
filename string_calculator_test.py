from unittest import TestCase

from string_calculator import StringCalculator


class TestStringCalculator(TestCase):
    def setUp(self) -> None:
        self.calculator = StringCalculator()

    def test_empty_string_return_zero(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_one_number_string(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_two_numbers_separated_by_comma(self):
        self.assertEqual(self.calculator.add("1,2"), 3)

    def test_more_than_two_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3"), 6)

    def test_new_line_as_separator(self):
        self.assertEqual(self.calculator.add("1,2\n3"), 6)

    def test_raises_error_separator_at_end(self):
        with self.assertRaises(ValueError) as e:
            self.calculator.add("1,2,")

        self.assertEqual(
            str(e.exception), "Separators are not allowed at the end of string"
        )

    def test_handle_different_delimiters(self):
        self.assertEqual(self.calculator.add("//|\n1|2|3"), 6)
