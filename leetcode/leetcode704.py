#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File  : leetcode704.py
Author: Lewis Lau
Date  : 2022/4/26
Desc  : 
"""

def search( nums: list[int], target: int) -> int:
    left = 0;
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    #nums = [-1,0,3,5,9,12]
    nums = [1,2,3,27,9,12]

    target = 5

    print(search(nums, target))
