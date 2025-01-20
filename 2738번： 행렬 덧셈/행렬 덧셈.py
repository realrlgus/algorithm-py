#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2738                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2738                           #+#        #+#      #+#     #
#    Solved: 2025/01/20 18:12:28 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n, m = map(int, input().split())

matrix = [[0 for _ in range(n)] for _ in range(m)]

for i in range(2):
    for k in range(m):
        nums = list(map(int, input().split()))
        for p in range(n):
            matrix[k][p] = matrix[k][p] + nums[p] 

for item in matrix:
    print(*item)



