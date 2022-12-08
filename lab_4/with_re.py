import time
import re
input = open('/Users/dasha/Desktop/a.json', 'r', encoding='utf-8')
output = open('/Users/dasha/Desktop/a.yaml', 'w', encoding='utf-8')

start_time = time.perf_counter()
strings = input.read().split('\n')
input.close()
for i in range(len(strings)):
    if '    ' in strings[i]:
        strings[i]=strings[i].replace('    ','',1)
    if ':' in strings[i]:
        strings[i] = re.sub('[{}"",]', '', strings[i])
        output.write('\n')
        output.write((strings[i]))
    else:
        continue
output.close()
print(time.perf_counter() - start_time)

