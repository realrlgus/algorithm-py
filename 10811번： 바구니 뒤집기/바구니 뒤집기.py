#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10811                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10811                          #+#        #+#      #+#     #
#    Solved: 2025/01/20 15:23:03 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n , m = map(int, input().split())

baskets = list(range(1, n + 1))

for i in range(m):
    a , b = map(int , input().split())
    baskets[a-1:b] = reversed(baskets[a-1:b])

print(*baskets)



