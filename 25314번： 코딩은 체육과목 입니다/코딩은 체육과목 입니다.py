#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25314                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25314                          #+#        #+#      #+#     #
#    Solved: 2025/01/20 13:29:46 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
long_arr = []

for i in range(0 , n // 4):
    long_arr.append('long')
long_arr.append('int')

print(' '.join(long_arr))


