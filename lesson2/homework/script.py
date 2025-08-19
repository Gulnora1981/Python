## homework 02
txt = 'MsaatmiazD'
txt[::2]


txt = "I'm John. I am from London"
txt[20:26]
txt = "Gulnora"
txt[::-1]

food1,food2,food3,food4,food5 = 'olma','anor','shaftoli','nok','uzum'

food3


ls = ['25','35']
msg = ' '.join(ls)
msg
def polindrom(word):
    if word == word [::-1]:
        print('bu polindrom')
    else:
        print('polindrom emas')

polindrom('alla')
txt = ["Guli",'Oydin',"Ozoda",'Saxzoda','Bekzod']
birinchi= txt[0]
orta= txt[2]
oxirgi= txt[4]
ajratilgan_txt= [birinchi,orta,oxirgi]

print(ajratilgan_txt)

spiska = ['Toshkent','Andijon', 'Moskva','Parij','Ashxabod']

if  'Parij' in spiska:
    print('bor')
else:
    print('yoq')      
        
#print(spiska)


ls = [10,20,30,40]
print(ls)
ls.append([50,60,70,80])
ls
raqamlar=[10,20,30,40,50,60]
raqamlar[0],raqamlar[-1]=raqamlar[-1],raqamlar[0]
print(raqamlar)
