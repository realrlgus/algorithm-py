#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3052                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3052                           #+#        #+#      #+#     #
#    Solved: 2025/01/20 15:17:24 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = lambda:sys.stdin.readline().rstrip() 

nums = {}

for i in range(10):
    num = int(input())
    divide = num % 42
    nums[divide] = nums.get(divide , 0) + 1



print(len(nums.keys()))
