#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1316                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1316                           #+#        #+#      #+#     #
#    Solved: 2025/01/20 17:35:59 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys = lambda:sys.stdin.readline().rstrip()

n = int(input())
total = 0

for _ in range(n):
    words = list(input())
    is_group = 1
    k = set()

    for i in range(len(words)):
        if words[i] in k:
            is_group = 0
            break
        if i == len(words) - 1:
            break

        if words[i] != words[i + 1]:
            k.add(words[i])
    total += is_group
        
print(total)




