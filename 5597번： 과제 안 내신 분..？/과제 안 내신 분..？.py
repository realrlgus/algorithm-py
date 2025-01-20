#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5597                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5597                           #+#        #+#      #+#     #
#    Solved: 2025/01/20 15:04:59 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = lambda: sys.stdin.readline().rstrip()

nums = [0] * 30

for line in sys.stdin:
    num = int(line) 
    nums[num - 1] = num

print(*[num + 1 for num in range(len(nums)) if nums[num] == 0], sep="\n")


