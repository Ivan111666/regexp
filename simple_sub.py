#!/usr/bin/env python3

# Для каждого регулярного выражения, которое требуется написать,
# указана строка, в которой нужно выполнить замену, а следом
# после стрелки (--->) указан результат замены

# bab ---> bzb
# bcb ---> bzb
# bxb ---> bzb
REGEXP_1 = r'b[acx]b'
REGEXP_1_REPL = r'bzb'

# abcXYZabc   ---> abcabc
# XaYbZcWaM   ---> abca
# abc XYZabc  ---> abc abc
REGEXP_2 = r'[A-Z]' 
REGEXP_2_REPL = r''

# abcABCabc  ---> abcABCabc
# DaEbFcAaB  ---> abcAaB
# abcXYZabc  ---> abcXYZabc
# XaYbZcZaY  ---> XaYbZcZaY
# DXEYFZabc  ---> XYZabc
# ADBECFXYZ  ---> ABCXYZ
REGEXP_3 = r'[DEF]'
REGEXP_3_REPL = r''

# abc0abc   ---> abcabc
# 1a2b3c4   ---> abc
# a123!@#bc ---> abc
REGEXP_4 = r'[^a-zA-Z]'
REGEXP_4_REPL = r''

# a,b,c d,e,f      ---> a_b_c_d_e_f
# abc!@#a          ---> abc___a
# abc!@#,./abc abc ---> abc______abc_abc
REGEXP_5 = r'[^a-zA-Z]'
REGEXP_5_REPL = r'_' 

# a abc aa bb  ---> a aa bb
# a def dd fd  ---> a dd fd
# x xy xyz yz  ---> x xy yz
# x xyz xyz yz ---> x yz
REGEXP_6 = r'\b[a-z]{3}\s'
REGEXP_6_REPL = r''

# AabcdZ ---> abcd
# BabcdC ---> BabcdC
# aAbZcd ---> aAbZcd
# AabcdY ---> abcdY
# BabcdZ ---> Babcd
REGEXP_7 = r'^A|Z$'
REGEXP_7_REPL = r''

# a b c  ---> a b c
# a  b c ---> a b c
# d    f ---> d f
REGEXP_8 = r'\s+'
REGEXP_8_REPL = r' '

# a ab abc abcd ab ---> a ab ab
# a xyz xyz a      ---> a a
# d xy xyza a      ---> d xy a
# a xyzzy b        ---> a xyzzy b
REGEXP_9 = r'\b(ab\w+|xyz\w{0,1})\b( )'
REGEXP_9_REPL = r''