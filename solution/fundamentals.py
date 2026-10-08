# ============================
# Question 1
# ============================
def pseudo_squares(n):
    for i in range(1, n + 1):
        print(i * i)


# ============================
# Question 2
# ============================
def sum_divisible_by_three(n) -> bool:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total % 3 == 0


# ============================
# Question 3
# ============================
def countdown_odd(n: int) -> None:
    while n >= 1:
        if n % 2 == 1:
            print(n)
        n -= 1


# ============================
# Question 4
# ============================
def check_passcode(passcode: str) -> str:
    if passcode == "":
        return "Invalid"
    if len(passcode) < 8:
        return "Weak"

    has_letter = any(c.isalpha() for c in passcode)
    has_number = any(c.isdigit() for c in passcode)
    has_symbol = any(c in "!@#$%^&*" for c in passcode)

    if has_letter and has_number and has_symbol:
        return "Strong"
    if has_letter and has_number:
        return "Medium"
    return "Weak"


# ============================
# Question 5
# ============================
def reverse_letters_in_words(sentence: str) -> str:
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)
