import icu
from os import listdir
from os.path import isfile, join

in_path = 'data/iterim'
txts = [f for f in listdir(in_path) if isfile(join(in_path, f))]

alphabet = []
for txt in txts:
    with open(join(in_path, txt), 'r') as f:
        chars = f.read()
        for e in chars:
            if e not in alphabet:
                alphabet.append(e)
# sort unicode
collator = icu.Collator.createInstance(icu.Locale('hu_HU.UTF-8'))
alphabet = sorted(alphabet, key=collator.getSortKey)
with open('data/meta/alphabet.txt', 'w') as f:
    for char in alphabet:
        f.write(char + '\n')
#TODO: a correct_chars befejezése
#TODO: a processed mappába írd ki a kijavított txt fájlokat