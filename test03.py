#รับค่า/ป้อนทางแป้นพิมพ์ ใช้ฟังชั่น input() โดยสิ่งที่ป้อนทั้งหมดคือs String

#ตัวแปร variable เป็น indentifier มีหน้าที่เก็บข้อมูลที่เกิดขึ้นในโปรเเกรม ข้อมูลที่เก็บจะอยู่ใน Ram
#indentifier คือชื่อที่ Dev. ตั้งขึ้นมาเอง ต้องเป็นไปตามกฏการตั้งช่อของภาษานั้นๆ

std_id = input('รหัสนักศึกษา : ')
std_name = input('ชื่อนักศึกษา : ')
stdYearBorn = input('ปีเกิด : ')
print('-------------------')
stdAge = 2023 - int(stdYearBorn) #ต้องแปลง Strinf เป็ร Nomber -> int(),float()
print(f'ยินดีตอนรับ {std_id} ชื่อ {std_name}')
print(f"คุณปีเกิด {stdYearBorn} อายุ {stdAge}")
print('-------------------')
print('ยินดีต้อนรับ',std_id,"ชื่อ",std_name)
print("คุณปีเกิด",stdYearBorn ,'อายุ',stdAge)
print('-------------------')
print('ยินดีต้อนรับ '+std_id+ " ชื่อ "+std_name)
print('คุณปีดเกิด '+stdYearBorn+ " อายุ "+str(stdAge))
print('-------------------')
print("ยินดีต้อนรับ {} ชื่อ {}".format(std_id,std_name))
print('คุณปีดเกิด {} อายุ {}'.format(stdYearBorn,stdAge))
print('-------------------')
print("ยินดีต้อนรับ %s ชื่อ %s" %(std_id,std_name))
print('คุณปีดเกิด %s อายุ %d' %(stdYearBorn,stdAge))
#------------#
