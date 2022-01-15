
from colorPairToNumber import MAJOR_COLORS, MINOR_COLORS

def showManual():
    colorValue = 1
    print('\n\n')
    print(f"{'COLOR-CODE':^12} | {'MAJOR COLOR':^13} | {'MINOR COLOR':^12}")
    for i in MAJOR_COLORS:
        for j in MINOR_COLORS:
            print(f"{colorValue:^12} | {i:^13} | {j:^12}")
            colorValue+=1
        print('-'*42)
