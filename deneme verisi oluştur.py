import random


f = open("tarihler.txt", "a")

haftanin_günleri = ("Mon ", 
                    "Tue ",
                    "Wed ",
                    "Thu ",
                    "Fri ",
                    "Sat ",
                    "Sun "
                    )
sayi = []
for i in range(3500):
    sayi.append(random.randrange(8, 23)) 
    

sayi.sort()
say = 0
hafta = 0
degiş = 1
for i in range(0,3500):
    
    if(i == 499 *degiş):
        say = say + 1
        degiş = degiş + 1
        print("---------",str(say))
        if(say == 7):
            break
           
    f.write(haftanin_günleri[say]+str(sayi[i])+"\n")
        

f.close()






























