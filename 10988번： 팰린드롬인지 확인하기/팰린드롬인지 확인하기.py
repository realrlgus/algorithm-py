#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10988                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10988                          #+#        #+#      #+#     #
#    Solved: 2025/01/20 16:49:39 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = lambda:sys.stdin.readline().rstrip()

s = input()

left , right = 0 , len(s) - 1
isPalindrom = 1

while left < right:
    if s[left] != s[right]:
        isPalindrom = 0
        break
    left = left + 1
    right = right - 1

print(isPalindrom)