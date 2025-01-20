#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10807                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10807                          #+#        #+#      #+#     #
#    Solved: 2025/01/20 13:58:21 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
k = list(map(int , input().split()))
v = int(input())

print(k.count(v))

    
