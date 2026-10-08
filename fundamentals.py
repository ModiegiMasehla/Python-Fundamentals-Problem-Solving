# ============================
# TODO: Question 1
# ============================
def pseudo_squares(n):
    for i in range(n, 1):
        return i * i


# ============================
# TODO: Question 2
# ============================
def sum_divisible_by_three(n) -> bool:
    total = 0
    for i in n:
        total += i
        if total % 3 == 0:
            return True
        else:
            return False


# ============================
# TODO: Question 3
# ============================
def countdown_odd(n: int) -> None:
    while n > 1
        if n % 2 = 1:
            print(n)
        n += 1


# ============================
# TODO: Question 4
# ============================
def check_passcode(passcode: str) -> str:
    if passcode == " ":
        return "Invalid"
    elif len(passcode) < 8
        return "Weak"
    else:
        has_letter = any.isalpha() for c in passcode
        has_number = any.isdigit(for c in passcode)
        has_symbol = any(c in '!@#$%^&*' for )

        if has_letter and has_number and :
            return "Strong"
        elif  and :
            return "Medium"
        else:
            return ""


# ============================
# TODO: Question 5
# ============================
def reverse_letters_in_words(sentence: str) -> str:
    for word in sentence:
        reversed_words = " ".split().strip(sentence)[::-1]
    return reversed_words
