import functions as f


class Test_functions:
    def test_sum(self):
        assert f.adding(2, 5) == 7

    def test_sum1(self):
        assert f.adding(2, 5) == 7

    def test_sum2(self):
        assert f.adding(2, 5) == 7

    def test_roman1(self):
        assert f.RomanNumerals.to_roman(30) == 'XXX'

    def test_roman2(self):
        assert f.RomanNumerals.from_roman('MMII') == 2002

    def test_valid1(self):
        string = '((()))'
        assert f.valid_parentheses(string) == True

    def test_valid2(self):
        string = '(((()))'
        assert f.valid_parentheses(string) == False

    def test_valid3(self):
        string = '(()())()'
        assert f.valid_parentheses(string) == True

    def test_valid4(self):
        string = ''
        assert f.valid_parentheses(string) == True