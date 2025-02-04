# knitting pattern gauge translator

I wrote this very simple python script to translate my (simple) knitting patterns across gauges. I hope someone may also find it useful. **This is for proportions only**, and not repeating designs like cables or lace. 

## Features:
* Smart gauge conversion: Pattern rounds up/down depending on previous roundings, to perserve total height/ width.

  * For example: if we rounded down 17.3 - > 17, and next rounding is 17.3, instead of rounding down to 17 again (and carrying a 0.6 debt), we round up to 18 (and maintain a -0.4 debt). In general we will maintain the minimal |debt|. See function "smartRoundUp".


* Calculating inc/ dec repeats: If you need to increase/decrease X stitches in Y rows, and it can be solved by mixing inc/dec once every 3/2/1 rows, the resulting pattern will also include the number of repeats required of each. The result will be made to make the change in steepness as gradual as possible


## Format of patterns:
The gauge will be translated **only** for the following terms:

Width only: 
* co \<s>
* inc \<s>
* dec \<s>

Height only: 
* stk \<r>

Width and Height: 
* gauge: \<s>, \<r>
* inc \<s> for \<r>

Other numbers and formats will **NOT** be translated and be kept as original.

## How to use:
In the folder  "patterns" place your pattern (of .txt format) there.
An example pattern is provided: "cardiganpattern.txt". 

In terminal run:
```powershell
>> python .\knit.py <.\patterns\patternName.txt>
```

Then when prompted, enter your gauge in \<stitches, rows> format.
The resulting pattern will be written to patterns folder under the name "[pattern name]\_new\_\[stitches]\_\[rows].txt"

Usage example:
```powershell
>> python .\knit.py .\patterns\cardiganpattern.txt
enter your gauge in the following format:
 stitches, rows
>> 22, 31
```

Make sure your pattern only includes terms that will work with the format. Unsupported terms will not have their gauge modified.

## Notes:
### Pattern:
The example pattern given is my personl pattern for a cardigan with set-in sleeves, it suits a Women's size xs-s. It is mostly seamed, with sleeves being casted on the bodice and then knit flat.

General guidlines:
- Knit front pieces
- Knit back piece. Instead of inc/ co in the middle back for each side, I just add double that value to one of the half pieces and then knit them together in the next row.
- Seam front and back, keep stitches live to rib the whole piece seamlessly.
- Cast on the stitches on the bodice. I also always add an extra stitch on each side as a seam allowance. Make sure to space the stitches evenly considering stitch/row ratio.
- I never do 50-50 divide to front and back, closer to 40-60. The short row shaping is vibes based, so I don't put it in my pattern until after knitting the first sleeve.
- Seam sleeves and rib. I like around 4-6 cm of rib, depends on yarn and rib pattern
- Knit collar and hem (rib) 
- Add button band or zipper.

### Personal Note:
This is my first time publishing something, and creating a readme for that. :tada: :tada: :tada: