"""找逆序数
在一个排列中，如果一对数的前后位置与大小顺序相反，即前面的数大于后面的数，那么它们就称为一个逆序。一个排列中逆序的总数就称为这个排列的逆序数。现在，给你一个N个元素的序列，请你判断出它的逆序数是多少。
要求：设计分析算法并编程实现。
"""


class Solution:
    def reversePairs(self, record: list[int]) -> int:
        return self.sort_and_count(record)

    def sort_and_count(self, ll: list[int]):
        """
        Input: ll(a list of integers)
        Output: num of reverse pairs in it(int)

        Using recursive/d.c.c strategy, inspired by merge sort(side effect).
        """

        # base case/terminal condition
        if len(ll) <= 1:
            return 0

        # divide
        lo, hi = ll[:len(ll)//2], ll[len(ll)//2:]

        # conquer, suppose till now, num_lo and num_hi have been sorted already
        num_lo = self.sort_and_count(lo)
        num_hi = self.sort_and_count(hi)

        # combine/merge
        ll_idx, lo_idx, hi_idx = 0, 0, 0
        num_merge = 0

        while lo_idx < len(lo) and hi_idx < len(hi):
            if lo[lo_idx] <= hi[hi_idx]:
                ll[ll_idx] = lo[lo_idx]
                lo_idx += 1
            else:
                ll[ll_idx] = hi[hi_idx]
                hi_idx += 1
                num_merge += len(lo) - lo_idx

            ll_idx += 1

        while lo_idx < len(lo):
            ll[ll_idx] = lo[lo_idx]
            lo_idx += 1
            ll_idx += 1

        while hi_idx < len(hi):
            ll[ll_idx] = hi[hi_idx]
            hi_idx += 1
            ll_idx += 1

        return num_lo + num_hi + num_merge

