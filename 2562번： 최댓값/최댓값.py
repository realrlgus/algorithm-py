#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2562                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2562                           #+#        #+#      #+#     #
#    Solved: 2025/01/20 14:31:06 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

max_num = 0
max_idx = 0
idx = 1

for line in sys.stdin:
    if int(line) > max_num:
        max_num = int(line)
        max_idx = idx
    idx = idx + 1

print(f'{max_num}\n{max_idx}')