'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        b_x = bin(x).split('b')[1]
        b_y = bin(y).split('b')[1]
        x, y = self.add_same_lenth(b_x, b_y)
        return self.compare_distance(x, y)


    def compare_distance(self, x, y):
        l = len(x)
        cnt = 0
        for i in range(l):
            if x[i] != y[i]:
                cnt += 1
        return cnt

    def add_same_lenth(self, x, y):
        minus = abs(len(x) - len(y))
        if len(x) < len(y):
            x = self.add_0_on_head(x, minus)
        else:
            y = self.add_0_on_head(y, minus)
        return x, y

    def add_0_on_head(self, h, num):
        for i in range(num):
            h = '0' + h
        return h
