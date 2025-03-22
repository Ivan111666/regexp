REGEXP_1 = r'^a[b]?$'

# + aab
# + abb
# + acb
# - ab
# - aabc
REGEXP_2 = r"^a[a-c]b$"

# + sofia.mp3
# + sofia.mp4
# - sofia.mp7
# - sofia.mp34
REGEXP_3 = r"^sofia\.mp[34]$"

# + taverna
# + versus
# + vera
# + zveri
# - zver
REGEXP_4 = r"^taverna|versus|vera|zveri$"

# - a
# - aa
# + aaa
# - aaaa
# - b
# - bb
# + bbb
# - bbbb
# - ccc
REGEXP_5 = r"^(a{3}|b{3})$"

# - Ok
# - OkOk
# + OkOkOk
# - OkOkOkOk
# - ab
# - abab
# + ababab
# - abababab
REGEXP_6 = r"^(Ok|ab){3}$"

# - aaa
# - aaa aaa
# + aaa Aaa aaa
# + aaa aaa Aaa
# + Aaa aaa aaa
# - A
# - aaa A aaa
REGEXP_7 = r"^(?=.*\bAaa\b)(?:\b[aA]{3}\b\s*){3}$"

# + abc
# + abc03
# + a-b-c-3
# + a.b.c.0
# - Aabc
# - abc1
# - #abc
REGEXP_8 = r'^a[.-]?b[.-]?c[.-]?([03])?([03])?$'