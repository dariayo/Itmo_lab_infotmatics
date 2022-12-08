import time
input = open('/Users/dasha/Desktop/a.json', "r", encoding="utf-8")
start_time = time.perf_counter()
text = input.read()
input.close()
text = text.replace('{', '')
text = text.replace('"', '')
text = text.replace('}', '')
text = text.replace(',', '')
levels = []
maxLevel = 0
text = text.split('\n')
text.pop(0)  #убираем первую строку
i = 0

for line in text:
    tabs = 0
    for symbol in line:
        if symbol != '\t':
            break
        tabs += 1
    if line.count('\t') == len(line):
        tabs = 1
    levels.append(tabs)
    maxLevel = max(maxLevel, tabs)


def testRUN():
    output = open('/Users/dasha/Desktop/a.yaml', "w", encoding="utf-8")
    for i in range(len(text)): #проходимся по файлу
        if '    ' in text[i]:
            text[i] = text[i].replace('    ', '', 1)
        output.write(text[i] + '\n')
    output.close()
    printFile = open('/Users/dasha/Desktop/a.yaml', "r", encoding="utf-8")
    text1 = printFile.read()
    print(text1)
testRUN()
print(time.perf_counter() - start_time)


