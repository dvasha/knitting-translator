
import numpy as np

def fitbt(arr, total, final, curr):
    if(total==0):
        final.append(arr[:])
        return final
    if (total<0):
        return final
    for i in range (curr, 24):
        arr.append(i)
        fitbt(arr, total-i, final, i)
        arr.pop()
    

def createTemplate(word, marker, lst, layout, final, i, j):
    print(f"{word} , {marker}, {lst}, {len(lst)}\n")
   
    if(len(lst)==0 and word==0):
        #no more words to fit, last word finished
        final.append([row[:] for row in layout])
        print("'---------------------------------------------")
        for row in layout: 
            print(" ".join(str(num) for num in row))
        print("'---------------------------------------------")

        return
    # go by longest word first, happens with pop
    if(word==0): # get new word and find next vacant stop
        word = lst.pop()
        marker = marker + 1
        for newi in range (0,6):
            for newj in range(0,8):
                if(layout[newi][newj] == 0):
                    i = newi 
                    j = newj 
                    break
    for di in range (-1,2):
        for dj in range (-1, 2):
            if (i+di >= 0 and i+di <6 and
                j+dj >= 0 and j+dj <8 and
                layout[i+di][j+dj] == 0):
                    layout[i+di][ j+dj] = marker
                    createTemplate(word-1, marker, lst, layout, final, i+di, j+dj)
                    layout[i+di] [j+dj] = 0
    


a =[]
arr = np.zeros((6,8), int)
fitbt([], 48, a, 3)
# print(a)


print(a[0])
final = []
createTemplate(0, 1, a[0], arr, final, 0, 0)
print(final[0])