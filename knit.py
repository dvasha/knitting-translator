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
                    f.write(f"for {newR} inc {newS}\n")
                case ["for", height, "dec", width]:
                    newR, remR = roundUp(float(height)*ratioR, remR)
                    newS, remS = roundUp(float(width)*ratioS, remS)
                    f.write(f"for {newR} dec {newS}\n")
                case ["inc", values]:
                    newS, remS = roundUp(float(width)*ratioS, remS)
                    f.write(f"inc {newS}\n")
                case ["dec", values]:
                    newS, remS = roundUp(float(width)*ratioS, remS)
                    f.write(f"dec {newS}\n")
      
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

def main():
    # currentgauge = getgauge()
    currentgauge = gauge(22,31)
    knittingpattern = getknittingpattern("./cardiganpattern.txt")
    knittingpattern.print()
    print(translateGauge(knittingpattern.knitgauge, currentgauge))
    translate(knittingpattern, currentgauge)
    
    


if __name__ == "__main__":
    main()