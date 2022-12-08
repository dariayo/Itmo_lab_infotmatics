import time
input = open('/Users/dasha/Desktop/a.json',  'r', encoding='utf-8')
output = open('/Users/dasha/Desktop/a.yaml', 'w', encoding='utf-8')

start_time = time.perf_counter()
strings = input.read().split('\n')
input.close()
for i in range(len(strings)):
    if '    ' in strings[i]:
        strings[i]=strings[i].replace('    ','',1)
    if '"' in strings[i]:
        strings[i]=strings[i].replace('"','',1)
    if '",' in strings[i]:
        strings[i]=strings[i].replace('",','"',1)
    if '\t' in strings[i]:
        strings[i]=strings[i].replace('\t','',1)
    if ':' in strings[i]:
        if '[' in strings[i]:
            strings[i]=strings[i].replace('[','',1)
        if ']' in strings[i]:
            strings[i]=strings[i].replace(']','',1)
        if '{' in strings[i]:
            strings[i]=strings[i].replace('{','',1)
        if '}' in strings[i]:
            strings[i]=strings[i].replace('}','',1)
        if '"' in strings[i]:
            strings[i]=strings[i].replace('"','',1)
        if ',' in strings[i]:
            strings[i]=strings[i].replace(',','',1)
        output.write('\n')
        output.write((strings[i]))
    else:
        continue
output.close()
print(time.perf_counter() - start_time)

