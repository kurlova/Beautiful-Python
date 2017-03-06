import time
import argparse
import os
import sys
from chainmap import ChainMap
from itertools import izip
from collections import defaultdict, deque


# ================= Looping over a collection =================================
colors = ['red', 'green', 'blue', 'yellow']

# bad
start_time = time.time()
for i in range(len(colors)):
    print colors[i]
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

# good
start_time = time.time()
for color in colors:
    print color
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

print('')

# ================= Looping backwards =========================================
colors = ['red', 'green', 'blue', 'yellow']

# bad
start_time = time.time()
for i in range(len(colors)-1, -1, -1):
    print colors[i]
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

# good
start_time = time.time()
for color in reversed(colors):
    print color
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

print('')

# ================= Looping over a collection and indicies ====================
colors = []
for i in xrange(20):
    colors.append('red')

# bad
start_time = time.time()
for i in range(len(colors)):
    print i, '-->', colors[i]
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

# good
start_time = time.time()
for i, color in enumerate(colors):
    print i, '-->', colors[i]
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

print('')

# ================= Looping over two collections ==============================
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

# bad
start_time = time.time()
n = min(len(names), len(colors))
for i in range(n):
    print names[i], '-->', colors[i]
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

# good
start_time = time.time()
for name, color in zip(names, colors):
    print name, '-->', color
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time
print zip(names, colors) # this is a list of tuples

# very good
start_time = time.time()
for name, color in izip(names, colors):
    print name, '-->', color
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time
print izip(names, colors) # this is an iterator

print('')

# ================= Looping in sorted order ===================================
colors = ['red', 'green', 'blue', 'yellow']

for color in sorted(colors):
    print color

for color in sorted(colors, reverse=True):
    print color

print('')

# ================= Custom sort order =========================================
colors = ['red', 'green', 'blue', 'yellow', 'white', 'cyan', 'ebony', 'pink',
          'magenta', 'purple', 'orange', 'lime', 'brown', 'black']

# bad
start_time = time.time()
def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0
print sorted(colors, cmp=compare_length)
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

# good
start_time = time.time()
print sorted(colors, key=len)
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

print('')

# ================= Call a function until a sentinel value ====================
"""
# bad
blocks = []
while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)

# good
blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)

with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        process_line(line)
"""
# ================= Distinguishing multiple exit points in loops ==============
seq = ['red', 'green', 'blue', 'yellow', 'white', 'cyan', 'ebony', 'pink',
          'magenta', 'purple', 'orange', 'lime', 'brown', 'black']
target = 'brown'

# BAD!!!!!!!! I KNOW LENA YOU LOVE IT
start_time = time.time()
def find(seq, target):
    found = False # flag variable, slows down the code
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i
print find(seq, target)
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

# GOOD
start_time = time.time()
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

# explaining
# for contains a if-else clause in it.
# For means: if I haven't finished the loop, keep doing the body.
# Else means: I've finished the body. Is there's anything more to do?
print find(seq, target)
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

print('')

# ================= Looping over dictionary keys ==============================
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

# printing keys
for k in d:
    print k

# printing values
for k in d.keys():
    print d[k]

#d = {k: d[k] for k in d if not k.startswith('r')}
#print d

# BAD: mutate (change)dictionary in a loop.(i'm not sure he meant this example)
# In general, it's BAD to CHANGE anything in a loop.
for k in d.keys():
    if k.startswith('r'):
        del d[k]

print('')

# ================= Looping over dictionary keys and values ===================
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red',
     'matthew1': 'blue1', 'rachel1': 'green1', 'raymond1': 'red1',
     'matthew2': 'blue2', 'rachel2': 'green2', 'raymond2': 'red2'}

# not so bad
start_time = time.time()
for k in d:
    print k, '-->', d[k]
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

# better but not good
start_time = time.time()
for k, v in d.items():
    print k, '-->', v
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

# good
start_time = time.time()
for k, v in d.iteritems():
    print k, '-->', v


elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

print('')

# ================= Construct a dictionary from pairs =========================
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

# good
d = dict(izip(names, colors)) # iter object to dict
print d

print('')

# ================= Counting with dictionaries ================================
colors = ['red', 'green', 'red', 'blue', 'green', 'red']

# bad, but it's good when teach people basic things
start_time = time.time()
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
print d
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

# good
start_time = time.time()
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
print d
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

# good... but requires knowlege
start_time = time.time()
d = defaultdict(int)
for color in colors:
    d[color] += 1
print d
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

print('')

# ================= Grouping with dictionaries -- Part I ======================
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

# bad
d = {}
start_time = time.time()
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)
print d
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

# normal, but setdefault looks scary. Considered as idiomatic Python earlier
d = {}
start_time = time.time()
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
print d
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

# good, an idiom of grouping in Python now
d = defaultdict(list)
start_time = time.time()
for name in names:
    key = len(name)
    d[key].append(name)
print d
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

print ('')

# ================= Atomic popitem() ==========================================
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

# good
while d:
    key, value = d.popitem() # popitem deletes values from dictionary
    print key, '-->', value
print d # it's empty

print ('')

# ================= Linking dictionaries (without real approval)===============
defaults = {'color': 'red', 'user': 'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args([])
command_line_args = {k:v for k, v in vars(namespace).items() if v}
# there must be one more dictionary with environ
# (but it was missed in presentation)

# common way
d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)

# better way
d = ChainMap(command_line_args, os.environ, defaults)

# ================= Clarify function calls with keyword arguments =============

# not good and not understandable
# twittersearch('@adele', False, 20, True)

# good
# twittersearch('@adele', retweets=False, numtweets=20, popular=True)

# Why? It's better to waste microseconds than hours of a programmer time

# ================= Clarify multiple return values with named tuples ==========

# not readable
# doctest.testmod()
# (0, 4)

# readable
# doctest.testmod()
# TestResults(failed=0, attempted=4)

# TestResults = namedtuple('TestResults', ['failed', 'attempted'])

# ================= Unpacking sequences =======================================
p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'

# bad
fname = p[0]
lname = p[1]
age = p[2]
email = p[3]

# good
fname, lname, age, email = p

# ================= Updating multiple state variables =========================

# bad
def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print x
        t = y
        y = x + y
        x = t

# very good way of thinking
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print x
        x, y = y, x+y

# ================= Simultaneous state updates ================================

# bad
def testfunc():
    tmp_x = x + dx * t
    tmp_y = y + dy * t
    tmp_dx = influence(m, x, y, dx, dy, partial='x')
    tmp_dy = influence(m, x, y, dx, dy, partial='y')
    x = tmp_x
    y = tmp_y
    dx = tmp_dx
    dy = tmp_dy

# good. excel is an analogy
def testfunc():
    x, y, dx, dy = (x + dx * t,
                    y + dy * t,
                    influence(m, x, y, dx, dy, partial='x'),
                    influence(m, x, y, dx, dy, partial='y'))

# ================= Concatenating strings =====================================
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

# bad
s = names[0]
for name in names[1:]:
    s += ', ' + name
print s

# good
print ', '.join(names)

# ================= Updating sequences ========================================
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

# all of them bad
del names[0]
names.pop(0)
names.insert(0, 'mark')

# good
# deque - list-like container with fast appends and pops on either end
names = deque(['raymond', 'rachel', 'matthew', 'roger',
               'betty', 'melissa', 'judith', 'charlie'])

del names[0]
names.popleft()
names.appendleft('mark')

# ================= Using decorators to factor-out administrative logic =======

# bad: mixing administartive and business logic together
# business: opening a url, returning a web page
# administrative: caching the page in a dictionary so data will be remembered
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page

# good: using decorators which can be reused later
def cache(func): # administrative logic is here
    saved = {}
    @wraps(func)
    def newfunc(*args):
        if args in saved:
            return newfunc(*args)
        result = func(*args)
        saved[args] = result
        return result
    return newfunc

# @cache # <---- commented just to avoid an error
def web_lookup(url):
    return urllib.urlopen(url).read() # business logic is here

# ================= Factor-out temporary contexts =============================
# bad
'''old_context = getcontext().copy()
getcontext().prec = 50
print Decimal(355) / Decimal(113)
setcontext(old_context)'''

# good
'''
with localcontext(Context(prec=50)):
    print Decimal(355) / Decimal(113)
'''

# ================= How to open and close files ===============================
# bad
f = open('mydata.txt', 'r')
try:
    data = f.read()
finally:
    f.close()

# good
with open('mydata.txt', 'r') as f:
    data = f.read()

# ================= Factor-out temporary contexts =============================
# bad
'''
with open('mydata.txt', 'w') as f:
    oldstdout = sys.stdout
    sys.stdout = f
    try:
        help(pow)
    finally:
        sys.stdout = oldstdout
'''
# good
'''
@contextmanager
def redirect_stdout(fileobj):
    oldstdout = sys.stdout
    sys.stdout = fileobj
    try:
        yield fileobj
    finally:
        sys.stdout = oldstdout

with open('mydata.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)'''

# ================= List Comprehensions and Generator expressions =============
# not good: shows how to do instead of what is needed
start_time = time.time()
result = []
for i in range(30):
    s = i ** 2
    result.append(s)
print sum(result)
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

# shows what is needed, but slower
start_time = time.time()
print sum([i**2 for i in xrange(30)])
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time

# good and as fast as first
start_time = time.time()
print sum(i**2 for i in xrange(30))
elapsed_time = time.time() - start_time
print 'result time,', elapsed_time
