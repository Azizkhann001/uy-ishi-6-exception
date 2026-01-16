from datetime import date

bugun=date.today()
yil=bugun.year
bayram=date(yil,9,1)
if bugun>bayram:
    bayram=date(yil+1,9,1)

qoldi=(bayram-bugun).days
print("Mustaqillik bayramigacha", qoldi, "kun qoldi")

