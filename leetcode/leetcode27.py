#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File  : leetcode27.py
Author: Lewis Lau
Date  : 2022/4/26
Desc  : 
"""


def removeElement(nums: list[int], val: int) -> int:
    slow=fast=0
    while fast < len(nums):
        if nums[fast]!=val:
            nums[slow]=nums[fast]
            slow+=1
        fast+=1
    return slow


if __name__ == "__main__":
    nums = [1,2,3,2,9,12]
    target = 2
    print(removeElement(nums, target))
