#!/usr/bin/env python3

# Для каждого регулярного выражения, которое требуется написать,
# указана строка, в которой нужно найти подстроки, а следом
# после стрелки (--->) указан список подстрок, которые нужно найти

# 1 a 1 2 b ---> a, b
# z 2 y     ---> z, y
REGEXP_1 = r'[a-zA-Z]'

# aaa bbb ccc ---> aaa, bbb, ccc
# ddd eee fgh ---> ddd, eee, fgh
# a1b c2d e3f ---> a1b, c2d, e3f
REGEXP_2 = r'\b[a-zA-Z0-9]+\b'

# a aa aaa ---> aa, aaa
# b bb bbb ---> bb, bbb
# a bb aaa ---> bb, aaa
REGEXP_3 = r'\b[a-zA-Z]{2,}\b'

# 1.1.1.1 aaaa bbbbb      ---> 1.1.1.1
# a.a.a.a bbbb 2.2.2.2    ---> 2.2.2.2
# 3.3.3.3 cccc 4.4.4.4    ---> 3.3.3.3, 4.4.4.4
# 255.23.0.1 cccc 4.4.4.4 ---> 255.23.0.1, 4.4.4.4
# 255.0.23.1 cccc 4.4.4.4 ---> 255.0.23.1, 4.4.4.4
REGEXP_4 = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

# aaa Abbb ccc ---> Abbb
# Aaa Abbb ccc ---> Aaa, Abbb
# Caa Cbb Accc ---> Accc
REGEXP_5 = r'\bA[a-z]+\b'

# a b c d e f ---> a, b, e, f
# abcdef      ---> a, b, e, f
# adf         ---> a, f
# acf         ---> a, f
REGEXP_6 = r'[abef]'

# aaa +1.0 bb              ---> +1.0
# aaa -1.0 bb              ---> -1.0
# aaa -123.234 bb +111.999 ---> -123.234, +111.999
REGEXP_7 = r'[+-]?\d+\.\d{1,3}'

# aaa 18-04-2016 bbb            ---> 18-04-2016
# aaa 18.04.2016 bbb            ---> 18.04.2016
# aaa 18-04-ABCD bbb 18.04.2016 ---> 18.04.2016
# aaa 18/04/ABCD bbb 18/04/2016 ---> 18/04/2016
# aaa 18/04/ABCD bbb 18/4/2016  ---> 18/4/2016
REGEXP_8 = r'\b\d{1,2}[-/.]\d{1,2}[-/.]\d{4}\b'
