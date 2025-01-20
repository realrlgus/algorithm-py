#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2941                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2941                           #+#        #+#      #+#     #
#    Solved: 2025/01/20 17:10:15 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = lambda:sys.stdin.readline().rstrip()

two_alpha = ["c=", "c-" , "d-" , "lj" , "nj" , "s=" , "z="]
three_alpha = ["dz="]

s = input()
i = 0
count = 0

while i < len(s):
    if i < len(s) - 2 and s[i: i + 3] in three_alpha:
        i += 3
    elif i < len(s) - 1 and s[i: i + 2] in two_alpha:
        i += 2
    else:
        i += 1
    count += 1

print(count)
