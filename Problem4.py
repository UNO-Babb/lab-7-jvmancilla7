#Problem4.py
#Project Euler problem 4

from NumberTests import isPalindrome
def main():
  
  palindrome = 0
  num1 = 100

  while num1 < 1000:
    num2 = 100

    while num2 < 1000:
      product = num1 * num2

      if isPalindrome (product):
        if product > palindrome:
          palindrome = product

      num2 += 1
    num1 += 1

  print(palindrome)

      

if __name__ == '__main__':
  main()