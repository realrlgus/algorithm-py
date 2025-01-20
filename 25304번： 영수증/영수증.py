#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25304                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: realrlgus <boj.kr/u/realrlgus>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25304                          #+#        #+#      #+#     #
#    Solved: 2025/01/20 13:25:17 by realrlgus     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
total_price = int(input())
total_qty = int(input())
sum_price = 0

for i in range(0 , total_qty):
    price , qty = map(int,input().split())
    sum_price += price * qty


print("Yes" if sum_price == total_price else "No")
    