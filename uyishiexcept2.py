from datetime import date
a=int(input("Yilingiz:"))
b=int(input("Oy:"))
c=int(input("Kun:"))

bugun=date.today()
malumot=date(a,b,c)
kun=(bugun-malumot).days




print(kun,"kun otdi")

