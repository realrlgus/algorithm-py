#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10809                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10809                          #+#        #+#      #+#     #
#    Solved: 2025/01/20 16:01:30 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = lambda:sys.stdin.readline().rstrip()

num = [-1] * (ord('z') - ord('a') + 1)

s = list(input())

for i in range(len(s)):
    m = ord(s[i]) - ord('a')
    if num[m] != -1:
        continue
    num[m] = i

print(*num)