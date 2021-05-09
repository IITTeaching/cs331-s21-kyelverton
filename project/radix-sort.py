import urllib
import urllib.request #import requests wasn't working for me, so I used this instead

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    b = book_to_words(book_url)
    return " ".join(i.decode("utf-8") for i in LSD_radix_sort(b))

def max_length(lst):
        m = len(lst[0])
        for i in lst:
            if m < len(i):
                m = len(i)
        return m

def LSD_radix_sort(lst):
    m = max_length(lst)
    for i in range(m):
        lst = rs(lst, i, m)
    return lst

def MSD_radix_sort(lst):
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
    
    return " ".join(i.decode("utf-8") for i in lst)

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

print("-" * 20)

r = radix_a_book()
prev = r.split()[0]
for i in r.split():
    if i < prev:
        print(i)
    prev = i
#nothing is printed so everything is in order

print("-" * 20)

r2 = MSD_radix_sort(book_to_words())
prev = r2.split()[0]
for i in r2.split():
    if i < prev:
        print(i)
    prev = i
#MSD works as well

print("-" * 20)
