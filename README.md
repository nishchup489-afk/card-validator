# 💳 Card Validator — Project 20 / 100 Python Live Projects

> A production-grade implementation of the **Luhn Algorithm (Mod 10)** for validating card-like identifiers.

---

## 🚀 Overview

This project validates:

* Credit Cards
* Debit Cards
* IMEI Numbers
* Government IDs
* Healthcare IDs
* Library / Transport Cards

All using a **single elegant mathematical system**.

---

## 🧠 The Origin of the Algorithm

The **Luhn Algorithm** was created in **1954** by **Hans Peter Luhn**, an IBM scientist.

### Why it exists

Before digital systems were reliable, data entry errors were common.

The algorithm was designed to:

* Detect **human typing mistakes**
* Prevent **invalid numbers from being processed**
* Add a lightweight **error-detection layer** (not security!)

⚠️ Important: It does NOT prevent fraud. It only checks if a number is *structurally valid*.

---

## 📍 Where it is used

* Banking systems (Visa, MasterCard)
* Telecom (IMEI numbers)
* Government ID systems
* Payment gateways

---

## ⚙️ How Luhn Algorithm Works

### Steps

1. Reverse the number
2. Double every second digit (from index 1)
3. If doubling gives >9, subtract 9
4. Sum all digits
5. If sum % 10 == 0 → VALID

---

## 🔢 Mathematical Example

Take number: **45690**

```
Original:     4 5 6 9 0
Reversed:     0 9 6 5 4

Step 2:
0 (9×2) 6 (5×2) 4
→ 0 (18) 6 (10) 4

Step 3:
0 (1+8) 6 (1+0) 4
→ 0 (9) 6 (1) 4

Step 4:
0 + 9 + 6 + 1 + 4 = 20

Step 5:
20 % 10 = 0 ✅ VALID
```

---

## 🧮 Visual Pattern Insight

Think of it like a rhythm:

```
Keep → Double → Keep → Double → Keep
```

And every overflow is "folded back" into a single digit.

---

## 🖥️ CLI Implementation (Python)

```python
def validator_compressed(n: str) -> bool:
    n = n.replace(" ", "").replace("-", "")

    if not n.isdigit():
        return False

    n = [int(d) for d in str(n)[::-1]]
    total = 0

    for i, d in enumerate(n):
        total += d if i % 2 == 0 else (d * 2 - 9 if d * 2 > 9 else d * 2)

    return total % 10 == 0
```

---

## 🌐 FastAPI Implementation

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CardInput(BaseModel):
    number: str


def luhn_check(n: str) -> bool:
    n = n.replace(" ", "").replace("-", "")

    if not n.isdigit():
        return False

    digits = [int(d) for d in n[::-1]]
    total = 0

    for i, d in enumerate(digits):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d

    return total % 10 == 0


@app.post("/validate")
def validate_card(data: CardInput):
    return {
        "input": data.number,
        "valid": luhn_check(data.number)
    }
```

---

## ⚠️ Common Mistakes (Don’t Mess This Up)

* ❌ Forgetting to reverse the number
* ❌ Doubling wrong index (off-by-one errors)
* ❌ Not cleaning input (spaces, dashes)
* ❌ Mis-handling >9 digits (must subtract 9)
* ❌ Thinking Luhn = security (it’s NOT)

---

## 🧱 Stack Used

* Python (CLI logic)
* FastAPI (Backend API)
* Jinja2 (Templating)
* Poetry (Dependency management)

---

## 🔗 Links

* GitHub: [https://github.com/nishchup489-afk/card-validator](https://github.com/nishchup489-afk/card-validator)
* Live App: [https://www.card-validator-pro.vercel.app](https://www.card-validator-pro.vercel.app)

---

## 🧭 Final Thoughts

This project is simple on the surface.

But it teaches something deeper:

> Elegant systems don’t need complexity — they need precision.

Master this, and you’re not just writing code.
You’re understanding **how real-world systems defend against chaos.**

---

## 📦 Explore More

👉 Visit other projects:
[https://github.com/nishchup489-afk/100-Python-Projects](https://github.com/nishchup489-afk/100-Python-Projects)
