from translate import Translator
matn=["salom", "dastur", 2.5, "yordam", 34, "kitob"]

tarjimon=Translator(to_lang="en", from_lang="uz")
yangi={}

for i in matn:
    if type(i)==str:
        yangi[i]=tarjimon.translate(i)


print(yangi)