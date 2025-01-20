#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9086	                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9086	                          #+#        #+#      #+#     #
#    Solved: 2025/01/20 15:53:23 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = lambda:sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    s = input()
    print(f"{s[0]}{s[-1]}")