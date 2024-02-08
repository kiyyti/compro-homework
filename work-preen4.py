#ex.4 order 
ordertb = int(input("The order for table: "))
print("Dish item: Hainanese chicken rice")
riceorder = int(input("How many: "))
print("Dish item: Beef noodles")
beeforder = int(input("How manu: "))
print("Dish item: Water")
water = int(input("How many: "))
total = water+beeforder+riceorder

print("=============================")
print(f"Order for Table {ordertb}")
print(f"* Hainanese chicken rice : {riceorder}")
print(f"* Beef noodles : {beeforder}")
print(f"* Water : {water}")
print(f"Total items : {total}")