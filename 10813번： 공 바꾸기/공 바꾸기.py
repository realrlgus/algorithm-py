#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10813                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10813                          #+#        #+#      #+#     #
#    Solved: 2025/01/20 14:50:42 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = lambda:sys.stdin.readline().rstrip()

n , m = map(int, input().split())

baskets = [num + 1 for num in range(n)] 

for i in range(m):
    j , k = map(int , input().split())
    temp = baskets[j - 1]
    baskets[j - 1] = baskets[k - 1]
    baskets[k - 1] = temp

print(*baskets)
