import urllib
import urllib.request #import requests wasn't working for me, so I used this instead

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    """Will radix sort a book using the msd radix sort. Will return an ordered list of strings."""
    b = book_to_words(book_url)
    return (i.decode("utf-8") for i in MSD_radix_sort(b))

def max_length(lst):
        m = len(lst[0])
        for i in lst:
            if m < len(i):
                m = len(i)
        return m

def LSD_radix_sort(lst):
    """Will radix sort a list of bytes starting from the least significant digit. Will return a list of bytes. Does not work with integers."""
    m = max_length(lst)
    for i in range(m):
        lst = rs(lst, i, m)
    return lst

def MSD_radix_sort(lst):
    """Will radix sort a list of bytes starting from the most significant digit. Will return a list of bytes. Does not work with integers."""
    def mrs(lst, pos):
        f = []
        c = [[] for _ in range(256)]
        for i in lst:
            if len(i) <= pos:
                c[0].append(i)
            else:
                p = i[pos]
                c[p].append(i)            
        for i in c:
            if len(i) > 1:
                if max_length(i) > pos:
                    i = mrs(i, pos + 1)
            f += i
        return f
    
    lst = mrs(lst, 0)
    
    return lst

def rs(lst, pos, ml):
    f = []
    c = [[] for _ in range(256)]
    for i in lst:
        if len(i) <= ml - pos - 1:
            c[0].append(i)
        else:
            p = i[ml - pos - 1]
            c[p].append(i)
    
    for i in c:
        f += i
    return f

def radix_ints(lst):
    """Will radix sort a list of integers starting from the least significant digit. Does not work with bytes."""
    m = max(lst)

    pos = 1
    while pos <= m:
        c = [[] for _ in range(10)]
        for i in lst:
            if pos > i:
                c[0].append(i)
            else:
                p = i // pos % 10
                c[p].append(i)
        
        lst = []
        for i in c:
            lst += i
        pos *= 10
    return lst

def radix_floats(lst):
    """Will radix sort a list of floats starting from the most significant digit. Does not work with bytes, but will work with integers. Has issues with numbers greater than 100000"""
    def mrs(lst, pos):
        def max_len(lst):
            m = lst[0]
            for i in lst:
                if len(str(i)) > len(str(m)):
                    m = i
            return m
        f = []
        c = [[] for _ in range(10)]
        for i in lst:
            if pos > i:
                c[0].append(i)
            else:
                p = int(round((i / pos % 10) * 10000) / 10000)
                c[p].append(i)            
        for i in c:
            if len(i) > 1:
                if max_len(i) / pos % 10 > 0:
                    i = mrs(i, pos / 10)
            f += i
        return f
    
    m = len(str(int(max(lst))))
    pos = 10 ** (m - 1)
    lst = mrs(lst, pos)
    
    return lst

print("Start")

r = " ".join(radix_a_book())
prev = r.split()[0]
for i in r.split():
    if i < prev:
        print(i)
    prev = i
#nothing is printed so everything is in order

print("Least Significant Radix Sort of a Book Completed")

r2 = " ".join(i.decode("utf-8") for i in LSD_radix_sort(book_to_words()))
prev = r2.split()[0]
for i in r2.split():
    if i < prev:
        print(i)
    prev = i
#MSD works as well

print("Most Significant Radix Sort of a Book Completed")

r3 = radix_ints(list(range(99999, -1, -1)))
for i in range(len(r3) - 1):
    if r3[i] > r3[i + 1]:
        print(i)
#integer sort works as well, and really fast

print("Least Significant Radix Sort of a List of Integers Completed")

r3 = radix_floats([i / 10 for i in range(99999, -1, -1)])
for i in range(len(r3) - 1):
    if r3[i] > r3[i + 1]:
        print(r3[i])
#float sort works, but rounding issues make my life annoying

print("Most Significant Radix Sort of a List of Floats Completed")
