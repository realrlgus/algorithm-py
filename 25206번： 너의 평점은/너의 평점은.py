#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25206                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25206                          #+#        #+#      #+#     #
#    Solved: 2025/01/20 17:56:43 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

grade = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0,
    'P' : 0.0,
}

total = 0
total_num = 0

for line in sys.stdin:
    _, a , b = line.split()
    if b == 'P':
        continue

    total_num += float(a)
    total += float(a) * grade[b]


print(f'{total / total_num:.6f}')