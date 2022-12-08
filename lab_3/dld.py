import re
print('Введите ваш ИСУ ')
isu: int = int(input())
eye: dict[int,str] = {0: ':', 1: ';', 2: 'X', 3: '8', 4: '=', 5: '['}
nose: dict[int,str] = {0: '-', 1: '<', 2: '-{', 3: '<{'}
mouth: dict[int,str] = {0: '(', 1: ')', 2: 'O', 3: '|', 4: '\\', 5: '/', 6: 'P'}

emoji: str=f"{eye[isu % 6]}{nose[isu % 4]}{mouth[isu % 7]}"
print(emoji)
test0 ='ajhd%^823{<[<Plask{[<P[<P'
test1= '278sj[<p[<P'
test2 = '289[<P3?>HTF[<P'
test3 = 'sakj7GDH/>&$#'
test4 = '[<P[<Pkjsa867[<Psj?>[<PR%^'
#test[0]=3 test[1]=1 test[2]=2 test[3]=0 test[4]=4
result = re.findall(r'\[<P',test0)
print(len(result))
