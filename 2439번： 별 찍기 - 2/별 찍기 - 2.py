#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2439                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2439                           #+#        #+#      #+#     #
#    Solved: 2025/01/20 13:50:06 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())

for i in range(1 , n + 1):
    print(" " * (n - i) + "*" * i)
