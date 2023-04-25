import random
def Loe_failist():
    with open('est.txt', 'r', encoding="utf-8-sig") as a:
        print(a.read())
    print()
    with open('rus.txt', 'r', encoding="utf-8-sig") as f:
        print(f.read())

def translate_sona(sona):
    with open('est.txt', 'r', encoding="utf-8-sig") as a, open('rus.txt', 'r', encoding="utf-8-sig") as f:
        est = [s.strip() for s in a.readlines()]
        rus = [s.strip() for s in f.readlines()]
    try:
        num = rus.index(sona)
        keel="rus"
        print(f'your translate is {est[num]}')
    except:
        try:
            num = est.index(sona)
            keel="est"
            print(f'your translate is {rus[num]}')
        except:
            valik=input("Your word not in dict. Want to add the word(yes/no): ")
            if valik=="yes":
                keel=input("est või rus: ") 
                translate=input("yr word on another language: ")
                with open('est.txt', 'w', encoding="utf-8-sig") as a, open('rus.txt', 'w', encoding="utf-8-sig") as f:
                    if keel=="est":
                        est.append(sona)
                        rus.append(translate)
                    else:
                        est.append(translate)
                        rus.append(sona)
                    for j in est:
                        a.write(j + "\n")
                    for i in rus:
                        f.write(i + "\n")
            return
    vitalik=input("Was the word correctly translated(yes/no): ")        
    if vitalik=="no":
        trl=input("Write correct word: ")
        if keel=="est":
            rus[num]==trl
            for i in rus:
                 f.write(i + "\n")
        else:
            est[num]==trl
            for j in est:
                 a.write(j + "\n")


def game():
    with open('est.txt', 'r', encoding="utf-8-sig") as a, open('rus.txt', 'r', encoding="utf-8-sig") as f:
        est = [s.strip() for s in a.readlines()]
        rus = [s.strip() for s in f.readlines()]
    choise=int(input('How many words do you want: '))
    oige=0
    for g in range(0,choise):
        if random.choice([True, False]):
            r1 = random.randint(0,len(est))
            va=input(f'write in russian translate of this word {est[r1]}: ')
            oige_vast=rus[r1]
        else:
            r1 = random.randint(0,len(rus))
            va=input(f'write in estonian translate of this word {rus[r1]}: ')
            oige_vast=est[r1]
        if va == oige_vast:
            oige+=1
            print("Great job")
        else:
            print(f'You are wrong.Right answer was {oige_vast}')
    print(f'Your accuransy is {oige / choise * 100} %')

game()

