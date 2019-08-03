# match greedy level 0
a = '%s' % '123'

# match greedy level 1
b = ('x' + '%s') % '123'

c = '%s'
# match greedy level 2
d = c % '123'

# false positive greedy level 1
e = '' + str(3 % 2)

# false positive greedy level 2
f = 3 % 2

# match greedy level 0
g = '{}'.format(123)

# match greedy level 1
h = ('x' + '{}').format(123)

i = '{}'
# match greedy level 2
j = i.format(123)


class C:
    def format(self):
        return ''


# false positive greedy level 1
k = '' + C().format()

# false positive greedy level 2
m = C().format()

# no errors below; coverage
''.strip()
