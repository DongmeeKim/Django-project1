import re


val = "01012341234" #11자리 휴대폰 번호
pattern = r"^01[016789][1-9]\d{6,7}$"
# 동일한 표현방식 : pattern = "^01[016789][1-9]\\d{6,7}$"

if re.match(pattern, val):
    print("matched")
else:
    print("invalied")