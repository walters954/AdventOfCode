__author__ = 'Walters954'

nice = 0
naughty = 0

naughty_nice_list = {'walters': True}
f = open('day5input.txt')

with open('day5input.txt', 'r') as f:
    for line in f:
        line = line.replace('\n', '')
        naughty_nice_list.update({line: True})
        for x in naughty_nice_list:
            for i in range(len(x) - 1):
                if x[i] == x[i + 1]:
                    naughty_nice_list[x] = True
                    break
                else:
                    naughty_nice_list[x] = False

            if naughty_nice_list[x]:
                if 'ab' in x or 'cd' in x or 'pq' in x or 'xy' in x:
                    naughty_nice_list[x] = False

            if naughty_nice_list[x]:
                if sum(x.count(i) for i in 'aeiou') < 3:
                    naughty_nice_list[x] = False

del naughty_nice_list['walters']


for x in naughty_nice_list.values():
    if x:
        nice += 1
    else:
        naughty += 1

print('Number of Naughty:', naughty)
print('Number of Nice:', nice)
print('Count: ', nice + naughty)
print('Count: ', len(naughty_nice_list))