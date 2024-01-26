# The pprint module allows us to better log on stdout

import pprint

message = 'it was a bright cold day in April, and the clocks werw striking'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
