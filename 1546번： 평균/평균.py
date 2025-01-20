#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1546                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1546                           #+#        #+#      #+#     #
#    Solved: 2025/01/20 15:45:07 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

nums = list(map(int , input().split()))
max_num = max(nums)
total = 0

for num in nums:
    total += num / max_num * 100

print(total / n)


