#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10810                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10810                          #+#        #+#      #+#     #
#    Solved: 2025/01/20 14:43:24 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

basket = [0] * n

for i in range(m):
    i , j , k = map(int, input().split())
    for p in range(i - 1 , j):
        basket[p] = k
    
print(*basket)
    
