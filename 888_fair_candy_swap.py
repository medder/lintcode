# -*- coding: utf-8 -*-
class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a_sum = sum(A)
        b_sum = sum(B)

        x = a_sum - b_sum

        sb = set(B)
        for i in A:
            s = int(i - x / 2)
            if s in sb:
                return [i, s]
