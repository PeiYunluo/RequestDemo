import re


# match = re.search(r'[1-9]\d{5}','BIT 100081 100001')
# if match:
#     print(match.group(0))

# match = re.match(r'[1-9]\d{5}','100081 100001 BIT')
# if match:
#     print(match.group(0))

# ls = re.findall(r'[1-9]\d{5}','')
# print(ls)

# ls = re.split(r'[1-9]\d{5}','BIT100081 TSU1001084',maxsplit= 1)
# print(ls)
#
# for m in re.finditer(r'[1-9]\d{5}','BIT100081 TSU1001084'):
#     print(m.span())

# str = re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 TSU1001084')
# print(str)

match = re.search(r'PY.*?N','PYANBNCNDN')
if match:
    print(match.group(0))