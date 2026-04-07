"""
 To validate Credit card , Debit card , IMEI number , Healthcare Provider ID , Government ID , Library cards or Transportation Card 
 A single Algorithm is used , created by IBM scientist Hans Peter Luhn in 1954 , "Luhn Algorithm" also known as "mod 10 algorithm"
 
 """


"""

Luhhn Algorithm:

  1) Reverse the number. After reversing , the first digit is `Check digit` (eg. 45690  -> 09654)
  2) Double Every second digit [ 0(9x2)6(5x2)4  -> 0(18)6(10)4]
  3) Reduce double digit number [ 0(1+8)6(1+0)4 -> 0(9)6(1)4 ] or substract 9 from double digit number [ 0(18-9)6(10-9)4 -> 0(9)6(1)4 ]
  4) sum all digits [ 0 +9 + 6 + 1 + 4 = 20 ]
  5) Check if the sum is divisible by 10 or not , if yes then valid , if not than invalid. [ 20%10 == 0 ]  ! valid

"""

number = input("Enter card / IMEI / ID: ").strip()


def validator(number : str) -> bool:
    number = str(number).replace(" " , "")

    if not number.isdigit():
        return False
    
    reversed_num = [int(digit) for digit in str(number)[::-1]]
    doubled_digits = []
    kept_digits = []

    for i , value in enumerate(reversed_num):

        

        if i%2 == 1:
            digit = value *2 
            if digit  > 9 :
                digit -=9

            doubled_digits.append(digit)


        else:
            kept_digits.append(value)


        
        
    total = sum(doubled_digits) + sum(kept_digits)

    if (total %10 == 0):
        return True
    else:
        return False
    






# COMPRESSED VERSION 


def validator_compressed(n : str) -> bool:
    n = n.replace(" ", "").replace("-", "")

    if not n.isdigit():
        return False
    
    n = [int(d) for d in str(n)[::-1]]
    total = 0

    for i , d in enumerate(n):
        total += d if i%2== 0 else ( d*2 -9 if d*2 > 9 else d*2)
    return total % 10 == 0



is_validated = validator_compressed(number)

if is_validated:
    print(f"{number} is Validated")
else:
    print(f"{number} is not validated")