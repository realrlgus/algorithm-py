#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3003                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3003                           #+#        #+#      #+#     #
#    Solved: 2025/01/20 16:41:45 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = lambda:sys.stdin.readline().rstrip()

chess = [1,1,2,2,2,8]
nums = list(map(int, input().split()))

for num in range(len(nums)):
    chess[num] = (-(nums[num] - chess[num]) if nums[num] > chess[num] else chess[num] - nums[num])
print(*chess)

