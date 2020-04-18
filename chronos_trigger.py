import time
import requests
from sys import argv


name = argv[1]

base_url = 'http://www.composure1.com/chronos/chronos_' + name + '_'

for i in range(1, 9999):
    test_url = base_url + str(i) + '.html'
    print(test_url)

    print(f'Testing {i}...')

    response = requests.get(test_url)
    # time.sleep(1)

    
    if response.ok:
        print(test_url)
        break

