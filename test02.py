#1. ใช้ ,
print("hello...",456,'hi...',True,10+20,"hey....")
#2. ใช้ + มีข้อเเม้ว่าทุกตัวที่เอามาต่อกันต้องเป็น String
print("Hello..."+str(456)+'Hi...'+str(True)+' '+str(20+10)+"Hey....")
#3. ใช้เมธอด Format
print('Hello{}Hi...{} {} Hay...'.format(456,True,10+20))
print('Hello{0}Hi...{1} {2} Hay...'.format(456,True,10+20)) #index number ตำเเหน่งข้อมูลในปีกกา
#4. ใช้ f-string
print(f"hello...{465} Hi... {True} {10+20} Hey...")
#5. ใข้ modular operator (%)-> %d, %f, %c, %s,....
print('Hello... %d Hi... %s %d Hay...' %(456,True,10+20) )