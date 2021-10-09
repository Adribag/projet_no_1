text = "■"


Prefix = "\x1b["
Style_Suffix = "m"
Reset = "0"
red = "1"
green = "2"
blue = "4"
FG_Prefix = "3"
# BG_Prefix = "4"
# Position_Suffix = "H"


# print (f"{Prefix}{FG};{BG}{Style_Suffix}{text}{Prefix}{Reset}{Style_Suffix}")
for i in range(1,10):
    print(f"{Prefix}{FG_Prefix}{red}{Style_Suffix}{text}{Prefix}{Reset}{Style_Suffix}")