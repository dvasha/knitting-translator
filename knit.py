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
def translate(knittingpattern, newgauge):
    ratioS, ratioR = translateGauge(knittingpattern.knitgauge, newgauge)
    
    with open("newpattern.txt", "w") as f:
        for line in knittingpattern.txtfile:
            # parsing here
            line = line.strip()
            match line.split():
                case ["gauge:", numS, numR]:
                    f.write(f"gauge: {float((numS.split(','))[0])*ratioS},{float(numR)*ratioR}\n")
                case ["co", values]:
                    f.write(f"co {float(values)*ratioS}\n")
                case ["stk", values]:
                    f.write(f"stk {float(values)*ratioR}\n")
                case ["for", height, "inc", width]:
                    f.write(f"for {float(height)*ratioR} inc {float(width)*ratioS}\n")
                case ["for", height, "dec", width]:
                    f.write(f"for {float(height)*ratioR} dec {float(width)*ratioS}\n")
                case ["inc", values]:
                    f.write(f"inc {float(values)*ratioS}\n")
                case ["dec", values]:
                    f.write(f"dec {float(values)*ratioS}\n")
      
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