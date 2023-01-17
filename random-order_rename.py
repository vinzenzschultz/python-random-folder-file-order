import os
import random

dateien = os.listdir()

zahlen = (list(range(0, 53)))
random.shuffle(zahlen)

for i in range(len(dateien)-1):
    wert = zahlen[i]
    teilen = dateien[wert].split('.')
    name = i + 100
    ende = str(name) + '.' + str(teilen[1])
    os.rename(str(dateien[wert]), str(ende))
