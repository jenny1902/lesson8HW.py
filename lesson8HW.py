import random
time = 0
apple = (int(input("請輸入有多少個蘋果🍎:")))
cost = (int(input("請輸入一個蘋果多少錢:")))
money = 200
deal = 0
while time < 1:
 q = (int(input("請問您要使用什麼功能? 1,設定 2,進貨 3,出貨 4,營業額統計 5,庫存 6,離開 :")))
 if q == 1:
    apple = (int(input("請輸入有多少個蘋果🍎:")))
    cost = (int(input("請輸入一個蘋果多少錢:")))
 if q == 2:
     n = random.randint(1, 2)
     if n == 1:
         print("抱歉~今天沒有人賣蘋果🍎~")
     else:
      in_apple = (int(input("請輸入要進多少蘋果🍎:")))
      money = money - (apple * cost)
      apple = apple + in_apple
      deal = deal + 1
     print("您現在有",money,"元")
     print("您現在有",apple,"顆蘋果🍎")
 if q == 3:
     spend = (int(input("請輸入您一顆蘋果想賣多少元:")))
     n = random.randint(1, 2)
     if n == 1:
         print("抱歉~今天沒有人要買蘋果🍎~")
     else:
      out_apple = (int(input("請輸入出了多少蘋果🍎")))
      money = money + (apple * spend)
      apple = apple - out_apple
      deal = deal + 1
     print("您現在有",money,"元")
     print("您現在有",apple,"顆蘋果🍎")
 if q == 4:
     print("您現在有",money,"元")
     print("您現在有",apple,"顆蘋果🍎")
     print("您現在做了",deal,"筆交易")
 if q == 5:
     print("您現在還有",apple,"顆蘋果🍎")
 if q == 6:
     print("結束營業!!")
     print("您現在有",money,"元")
     print("您現在有",apple,"顆蘋果🍎")
     print("您今天做了",deal,"筆交易")
     break