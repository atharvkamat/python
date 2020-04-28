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
def convertfive(minteger):
    c = int(minteger)
    d = {'0':'5','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}
    y = str(c)
    u = ""
    for x in range(0,lenght(y)):
        u += d[y[x]]
    return u
