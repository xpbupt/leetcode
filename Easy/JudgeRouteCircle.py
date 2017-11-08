'''
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
'''
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        UDLR = self.counts(moves)
        if UDLR['U'] == UDLR['D'] and UDLR['L'] == UDLR['R']:
            return True
        else:
            return False
        
    def counts(self, moves):
        u = 0
        d = 0
        l = 0
        r = 0
        c2d = {'U': 0,
               'D': 0,
               'L': 0,
               'R': 0}
        for d in moves:
            c2d[d] += 1
        return c2d
