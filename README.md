# Sum-of-Digits

This Python program calculates the **sum of all digits** in a given number entered by the user.

---

## 📌 What It Does

- Prompts the user to enter a number.
- Extracts each digit from the number.
- Adds all the digits together.
- Displays the final sum.

---

## 🧠 How It Works

1. The user is asked to input an integer.
2. A `while` loop runs as long as the number (`n`) is greater than 0:
   - The last digit is extracted using `n % 10`.
   - The digit is added to a running sum.
   - The number is reduced using integer division `n // 10`.
3. The result is printed at the end.

---
## 🚀 How To Run

python sum-digits.py

