# Western-to-classical-note-convertor
An attempt to convert western music notes written in A B C to carnatic (Indian classical) music notation in Sa Ri Ga.

![octaves of C](/future/octaves_of_C.png)

The script abc2srg takes in a text file with western notation(with  appropriate octaves) and translates them to a text file with carnatic notations (out.txt) at 3 kattai(E is Sa).


Parameters being passed are name of the input file and desired pitch shift (conversion will be irrespective of scale)

sample call:

```
python3 abc2srg.py
```
Converts file in.txt to out.txt with 0 pitch shift.

Sample Conversion:

```E3  F3  F3#``` gets converted to ```Ṣ Ṛ1 Ṛ2```