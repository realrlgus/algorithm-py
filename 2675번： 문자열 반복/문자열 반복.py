#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2675                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2675                           #+#        #+#      #+#     #
#    Solved: 2025/01/20 16:15:31 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = lambda:sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    a , b = input().split()
    m = ""
    for s in b:
        m += (s * int(a))
    print(m)

