import functools
from statistics import median
class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value % 2 != 0

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return self.value % 2 == 0

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        for i in range(2, int(self.value**0.5)+1):
            if self.value % i == 0:
                return False
        return True

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        return list(i for i in range(1, self.value) if self.value % i == 0)

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(str(self.value))

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        return functools.reduce(lambda x,y: int(x)+int(y), str(self.value))

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        return int(str(self.value)[::-1])

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        return self.value == int(str(self.value)[::-1])

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        return list(map(int, list(str(self.value))))

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        return max(list(map(int, list(str(self.value)))))
        

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        return min(list(map(int, list(str(self.value)))))

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        return sum(list(map(int, list(str(self.value)))))/len((list(map(int, list(str(self.value))))))

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        return median(map(int, (list(str(self.value)))))
        
        

    def get_range(self):
        """
        Returns the range of all the digits in the number.
        returns: list
        """
        items = list(map(int, (list(str(self.value)))))
        return [min(items), max(items)]
    
    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        items = list(map(int, (list(str(self.value)))))
        count_items = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        for i in items:
            if i not in count_items:
                count_items.update({i:1})
            else:
                count_items[i] += 1
        return count_items
        
# Create a new instance of Number
number = Number(1291)

print(number.get_frequency())