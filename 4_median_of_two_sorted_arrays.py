#!/usr/bin/env ipython3

# Author : james

# Date   : 11/11/2022 23:03:30


'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''



def solve(nums1, nums2):

    merged_list = []

    i = 0

    j = 0

    while i < len(nums1) or j < len(nums2):

        if i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:

                merged_list.append(nums1[i])

                i += 1

            else:

                merged_list.append(nums2[j])

                j += 1

        elif i < len(nums1):

            merged_list.append(nums1[i])

            i += 1

        elif j < len(nums2):

            merged_list.append(nums2[j])

            j += 1


    median_index = len(merged_list) // 2

    # odd
    if len(merged_list) % 2 != 0:

        median = merged_list[median_index]
    
    # even
    else:

        median = (merged_list[median_index - 1] + merged_list[median_index]) / 2

    return median


    # merged_list = sorted(nums1 + nums2)

    # from statistics import median

    # median = median(merged_list)

    # return median




if __name__ == '__main__':
    
    inputs  = [[[1,3], [2]],
               [[1,2], [3,4]],
              ]

    answers = [2, 2.5]

    for index, each_input in enumerate(inputs):

        my_result = solve(each_input[0], each_input[1])

        if my_result == answers[index]:

            print(f'PASS - {my_result} == {answers[index]}')

        else:

            print(f'FAIL - {my_result} != {answers[index]}')




