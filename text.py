
sjtx = [4,1,7,2,5,8,3,6,9]
number = 0
for wm in range(len(sjtx)):
    for lm in range(len(sjtx)):
        number = sjtx[wm]
        if sjtx[lm]>sjtx[wm]:
            sjtx[wm] = sjtx[lm]
            sjtx[lm] = number

for i in sjtx:
    print(i)


sjtx = [4,1,7,2,5,8,3,6,9]
number = 0
for wm in range(len(sjtx)):
    i = wm
    while i < len(sjtx):
        number = sjtx[wm]
        if sjtx[i]<sjtx[wm]:
            sjtx[wm] = sjtx[i]
            sjtx[i] = number
        i+=1

for i in sjtx:
    print(i)