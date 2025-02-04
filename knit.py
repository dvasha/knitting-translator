import math
class gauge:
    stitches = 0
    rows = 0
    
    def __init__(self, stitches, rows):
        self.stitches = int(stitches)  # Ensure integer conversion
        self.rows = int(rows)
    def print(self):
        print(self.rows, self.stitches)
class knittingpattern():
    def __init__(self, txt, gauge):
        self.txtfile = txt
        self.knitgauge = gauge

    def print(self):
        print(vars(self.knitgauge))
  
def roundUp(floatVal, rem):
    decimal = rem + floatVal - math.floor(floatVal)
    if (decimal < 0.5):
        resultint = math.floor(floatVal)
        rem = decimal 
    else :
        resultint = math.ceil(floatVal)
        rem = 1 - decimal 
    return resultint, rem

def translateGauge(oldGauge : gauge, newGauge : gauge):
    ratioS = float(1) / oldGauge.stitches * newGauge.stitches
    ratioR = float(1) / oldGauge.rows * newGauge.rows
    return ratioS, ratioR
def translate(knittingpattern, newgauge: gauge):
    ratioS, ratioR = translateGauge(knittingpattern.knitgauge, newgauge)
    remS, remR = 0, 0
    with open("newpattern.txt", "w") as f:
        for line in knittingpattern.txtfile:
            # parsing here
            line = line.strip()
            match line.split():
                case ["gauge:", _, _]:
                    f.write(f"gauge: {newgauge.stitches},{newgauge.rows}\n")
                case ["co", values]:
                    newS, remS = roundUp(float(values)*ratioS, remS)
                    f.write(f"co {newS}\n")
                case ["stk", values]:
                    newR, remR = roundUp(float(values)*ratioR, remR)
                    f.write(f"stk {newR}\n")
                case ["for", height, "inc", width]:
                    newR, remR = roundUp(float(height)*ratioR, remR)
                    newS, remS = roundUp(float(width)*ratioS, remS)
                    f.write(f"for {newR} inc {newS}:\n")
                    x,y, z = calculateFor(newR, newS)
                    if(x<0):
                        f.write(f"!!!!!! WIDTH > HEIGHT -- implement in python or handle manually !!!!!!\n")
                    else:
                        if(x>0):
                            f.write(f"\t inc 1 every 3 rows {x} times \n")
                        if(y>0):
                            f.write(f"\t inc 1 every 2 rows {y} times \n")
                        if(z>0):
                            f.write(f"\t inc 1 every row {z} times \n")
                case ["for", height, "dec", width]:
                    newR, remR = roundUp(float(height)*ratioR, remR)
                    newS, remS = roundUp(float(width)*ratioS, remS)
                    f.write(f"for {newR} dec {newS}:\n")
                    x,y, z = calculateFor(newR, newS)
                    if(x<0):
                        f.write(f"!!!!!! WIDTH > HEIGHT -- implement in python or handle manually !!!!!!\n")
                    else:
                        if(x>0):
                            f.write(f"\t dec 1 every 3 rows {x} times \n")
                        if(y>0):
                            f.write(f"\t dec 1 every 2 rows {y} times \n")
                        if(z>0):
                            f.write(f"\t dec 1 every row {z} times \n")
                case ["inc", values]:
                    
                    newS, remS = roundUp(float(values)*ratioS, remS)
                    f.write(f"inc {newS}\n")
                case ["dec", values]:
                    newS, remS = roundUp(float(values)*ratioS, remS)
                    f.write(f"dec {newS}\n")
                case [rest]:
                    f.write(f"{rest}\n")
      
def getknittingpattern(patternname):
    with open(patternname, "r") as f:
        txt = f.readlines()
    firstline = txt[0]
    gaugematch = firstline.split(':')[1].split(',')
    s, r = float(gaugematch[0].strip()), float(gaugematch[1].strip())
    knitgauge = gauge(s,r)
    return knittingpattern(txt, knitgauge)
 
def getgauge():
    string = input('enter your gauge in the following format:\n stitches, rows\n')
    x, y = string.split(',')
    return gauge(float(x), float(y)) 

def maxDiff(a,b,c):
    lst = [abs(a-b), abs(b-c)]
    return max(lst)

# W <= H <= 3 W 
#optimal solution such that 3x+2y+z=Height and x+y+z=Width, with x<=y<=z and difference between x-y, y-z are minimal/ 
def calculateFor(H, W):
    if H < W:
        print(H,W)
        raise Exception("unimplemented!") #need to create more advances function to allow such cases
    # print(H, W);
    minDiff = W
     # the maximal one would be when z=w and everyone else is 0
    minX, minY, minZ = -1,-1,-1
    #minimal diff algo
    for x in range(0,W+1):
        for y in range (0, W+1):
            z = W - x - y 
            if(z<0):
                continue
            if (3*x + 2*y + z == H):
                currDiff = maxDiff(x,y,z)
                # print(f"{x},{y},{z}, {currDiff}  \n{minX}, {minY}, {minZ}, {minDiff} \n")
                if (currDiff <= minDiff):
                    minX = x 
                    minY = y 
                    minZ = z 
                    minDiff = currDiff

    return minX, minY, minZ
    #if values are negative, there is no solution for this, therefore an extra value (w) should be added such that:
    # 4w + 3x + 2y + z = H
    # w + x + y + z = W
    # currently no need, since such shallow tapers do not exist in my patterns.
    # I will note that cases where W > H do exist in my knitting, but rarely and I would rather handle them manually.
        


    


def main():
    # currentgauge = getgauge()
    currentgauge = gauge(22,31)
    knittingpattern = getknittingpattern("./cardiganpattern.txt")
    knittingpattern.print()
    print(translateGauge(knittingpattern.knitgauge, currentgauge))
    translate(knittingpattern, currentgauge)
    
    
# for w in range (1, 200):
#     for h in range (w, 3*w+1):
#         res = calculateFor(h, w)
#         if (res[0] == -1):
#             print("ERROR for: {h}, {w}.\n")


if __name__ == "__main__":
    main()

    #21 or 15 + 6 14 + 3 + 4 15+2 14 + 1 + 2