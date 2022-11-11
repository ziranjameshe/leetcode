#!/usr/bin/env ipython3

# Author : james

# Date   : 11/11/2022 23:03:30


'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''



def solve(s):

    all_sub_strings = [0]

    sub_string      = ''

    for index, current_char in enumerate(s):

        if current_char not in sub_string:

            sub_string += current_char

            all_sub_strings.append(len(sub_string))

        else:

            duplicate_index = sub_string.index(current_char)

            sub_string      = sub_string[duplicate_index + 1 : index + 1]

            sub_string     += current_char

    all_sub_strings.append(len(sub_string))

    return max(all_sub_strings)



if __name__ == '__main__':
    
    inputs  = ['abcabcbb', 'bbbbb', 'pwwkew', '', ' ', "dvdf", 'ckilbkd', "ohvhjdml", "aabaab!bb"]

    answers = [3, 1, 3, 0, 1, 3, 5, 6, 3]

    for index, each_input in enumerate(inputs):

        my_result = solve(each_input)

        if my_result == answers[index]:

            print(f'PASS - {my_result} == {answers[index]}')

        else:

            print(f'FAIL - {my_result} != {answers[index]}')




