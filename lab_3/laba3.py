import re
print('Введите ваш ИСУ ')
isu: int = int(input())
eye: dict[int,str] = {0: ':', 1: ';', 2: 'X', 3: '8', 4: '=', 5: '['}
nose: dict[int,str] = {0: '-', 1: '<', 2: '-{', 3: '<{'}
mouth: dict[int,str] = {0: '(', 1: ')', 2: 'O', 3: '|', 4: '\\', 5: '/', 6: 'P'}

emoji = (eye[isu % 6])+(nose[isu % 4])+(mouth[isu % 7])
print(emoji)
test = ['[<P[<P[<P[<P[<P[<P[<P', '278sj[<p[<P','289[<P3?>HTF[<P', 'sakj7GDH/>&$#', '[<P[<Pkjsa867[<Psj?>[<PR%^']
#test[0]=7 test[1]=1 test[2]=2 test[3]=0 test[4]=4
a = re.compile(r'\[<P')
result = a.findall(test[1])
print(len(result))


    