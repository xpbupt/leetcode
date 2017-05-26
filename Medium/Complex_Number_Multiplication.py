'''
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
'''

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        t_a = self.get_real_and_complex(a)
        t_b = self.get_real_and_complex(b)
        c = self.calculate(t_a, t_b)
        return c[0] + '+' + c[1] +'i'
        
    def get_real_and_complex(self, c):
        a = c.split('+')[0]
        b = c.split('+')[1].split('i')[0]
        return (int(a), int(b))
        
    def calculate(self, a, b):
        return (str(a[0]*b[0] - a[1]*b[1]), str(a[0]*b[1] + a[1]*b[0]))
