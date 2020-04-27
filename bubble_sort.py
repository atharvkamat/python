num_test_cases = int(input())
def lenght(list_or_string):
    try:
        c = True
        y = 0
        while c== True:
            y=y+1
            u = list_or_string[y]
    except IndexError:
        c= False
    return int(y)
def co(s):
    str1 = [int(x) for x in s.split(' ') ]
    return str1
def d(sty):
    li1 = ' '
    li = ' '.join([str(e) for e in sty])
    return li
def num_finder(mylist):
    indexlen = lenght(mylist)
    yq=indexlen+1
    n=indexlen-1 
    for i in range(yq):
        u = -i+n
        for j in range(u-2):
            if mylist[j]>mylist[j+1]:
                mylist[j],mylist[j+1] = mylist[j+1],mylist[j]
         print(mylist)
    return mylist

for i in range(0,num_test_cases) :
    wnum_elements = input()
    in_string = input()
    my_list = co(in_string)
    print(d(num_finder(my_list)))
