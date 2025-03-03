#Problem7.py
#Project Euler problem 7

from NumberTests import isPrime


def main():
  found = 1
  p = 2

  while found < 10001:
    p =  p + 1
    if isPrime (p):
        found = found + 1
        prime = p
    

    
  print(prime)

if __name__ == '__main__':
  main()