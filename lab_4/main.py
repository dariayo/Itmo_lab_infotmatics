import json
import yaml
import time
start_time = time.perf_counter()
print(yaml.dump(json.load(open('/Users/dasha/Desktop/a.json')),allow_unicode=True))
print(time.perf_counter() - start_time)

