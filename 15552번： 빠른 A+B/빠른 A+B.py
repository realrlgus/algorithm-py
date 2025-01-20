#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15552                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15552                          #+#        #+#      #+#     #
#    Solved: 2025/01/20 13:34:31 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

for i in range(0, n):
    a , b = map(int , input().split())
    print(a + b)

