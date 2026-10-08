import fundamentals as fun


def run_and_capture(func, arg, capsys):
    capsys.readouterr()
    func(arg)
    out = capsys.readouterr().out.strip()
    return out.split("\n") if out else []


class TestFunctions:

    # ---------- Question 1 ----------
    def test_pseudo_squares_function_exists(self):
        assert callable(getattr(fun, "pseudo_squares", None)), \
            "Function 'pseudo_squares' is not defined"

    def test_pseudo_squares_output(self, capsys):
        test_cases = [
            (1, ["1"]),
            (3, ["1", "4", "9"]),
            (5, ["1", "4", "9", "16", "25"]),
            (7, ["1", "4", "9", "16", "25", "36", "49"]),
            (10, ["1", "4", "9", "16", "25", "36", "49", "64", "81", "100"]),
        ]
        for n, expected in test_cases:
            output = run_and_capture(fun.pseudo_squares, n, capsys)
            assert output == expected, \
                f"'pseudo_squares({n})' expected {expected}, got {output}"

    # ---------- Question 2 ----------
    def test_sum_divisible_by_three_returns_correctly(self):
        for n in range(1, 31):
            total = n * (n + 1) // 2
            expected = total % 3 == 0
            result = fun.sum_divisible_by_three(n)
            assert result == expected, (
                f"'sum_divisible_by_three({n})' should return {expected}. "
                f"Sum is {total}")

    def test_sum_divisible_by_three_returns_bool(self):
        assert isinstance(fun.sum_divisible_by_three(4), bool), \
            "'sum_divisible_by_three' must return a bool"

    # ---------- Question 3 ----------
    def test_countdown_odd_output(self, capsys):
        test_cases = [
            (10, ["9", "7", "5", "3", "1"]),
            (7, ["7", "5", "3", "1"]),
            (5, ["5", "3", "1"]),
            (8, ["7", "5", "3", "1"]),
            (1, ["1"]),
            (2, ["1"]),
            (0, []),
            (15, ["15", "13", "11", "9", "7", "5", "3", "1"]),
        ]
        for n, expected in test_cases:
            output = run_and_capture(fun.countdown_odd, n, capsys)
            assert output == expected, \
                f"'countdown_odd({n})' expected {expected}, got {output}"

    # ---------- Question 4 ----------
    def test_invalid_passcode(self):
        assert fun.check_passcode("") == "Invalid", \
            "Empty passcodes must return 'Invalid'"

    def test_weak_passcode_short(self):
        assert fun.check_passcode("abc") == "Weak"
        assert fun.check_passcode("1234567") == "Weak"
        assert fun.check_passcode("a1!") == "Weak"

    def test_weak_passcode_single_type(self):
        assert fun.check_passcode("abcdefgh") == "Weak"
        assert fun.check_passcode("12345678") == "Weak"

    def test_medium_passcode(self):
        assert fun.check_passcode("abcd1234") == "Medium"
        assert fun.check_passcode("Password1") == "Medium"

    def test_strong_passcode(self):
        assert fun.check_passcode("abcd123!") == "Strong"
        assert fun.check_passcode("P@ssw0rd#2026") == "Strong"

    # ---------- Question 5 ----------
    def test_reverse_letters_function_exists(self):
        assert callable(getattr(fun, "reverse_letters_in_words", None)), \
            "Function 'reverse_letters_in_words' is not defined"

    def test_reverse_letters_output(self):
        assert fun.reverse_letters_in_words("hello world") == "olleh dlrow"
        assert fun.reverse_letters_in_words("  This   is  a test  ") == "sihT si a tset"

    def test_reverse_letters_single_word(self):
        assert fun.reverse_letters_in_words("Python") == "nohtyP"

    def test_reverse_letters_empty_string(self):
        assert fun.reverse_letters_in_words("") == ""
