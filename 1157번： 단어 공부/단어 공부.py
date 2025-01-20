#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1157                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1157                           #+#        #+#      #+#     #
#    Solved: 2025/01/20 16:58:53 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = lambda: sys.stdin.readline().rstrip()

words = {}
for char in input().lower():
    words[char] = words.get(char, 0) + 1

max_count = max(words.values())
result = '?' if list(words.values()).count(max_count) > 1 else max(words, key=words.get).upper()
print(result)


