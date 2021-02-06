
from math import sqrt

class Numbers:
    ''' Contains frequently used methods for numbers '''

    def isPrime(self, num):
        if num <= 1:
            return False
        for divisor in range(2, int(sqrt(num)+1)):
            if num%divisor == 0:
                return False
        return True

    def isArmstrong(self, num):
        sum, num_clone = 0, num
        while(num > 0):
            reminder = num%10
            sum += (reminder**3)
            num = num//10
        return num_clone == sum
