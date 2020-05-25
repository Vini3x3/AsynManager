import urllib.request
import os
from tabulate import tabulate
from asyn_manager import test_suite

fp = urllib.request.urlopen("http://www.python.org")
html_bytes = fp.read()

html_str = html_bytes.decode("utf8")
fp.close()

print(html_str)

SAMPLE_DIR = 'sample/'

result = {}

with os.scandir(SAMPLE_DIR) as entries:
    for entry in entries:
        if entry.is_file():
            result[entry.name] = ''

for file in result:
    with open(os.path.join(SAMPLE_DIR, file), "r") as f:
        result[file] = len(f.readlines())

for key, val in result.items():
    print(key, val)


@test_suite.log('warn', '01', 'this is a warning')
@test_suite.timed_test()
def hi(a=12):
    print(1/a)


test_suite.print_log('doublesep')
