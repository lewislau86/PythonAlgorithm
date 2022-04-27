#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File  : leetcode283.py
Author: Lewis Lau
Date  : 2022/4/27
Desc  : 
"""


def moveZeroes(nums: list[int]) -> None:
    slow = fast = 0
    while fast < len(nums):
        if nums[fast] != 0:
            nums[fast], nums[slow] = nums[slow], nums[fast]
            slow += 1
        fast+= 1

    return slow


if __name__ == "__main__":
    nums = [1, 2, 0, 0, 9, 12]

    print(moveZeroes(nums))
