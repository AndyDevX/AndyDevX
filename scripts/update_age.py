import re
from datetime import date

BIRTH = date(2003, 9, 30)
today = date.today()
age = today.year - BIRTH.year - ((today.month, today.day) < (BIRTH.month, BIRTH.day))

with open("README.md", encoding="utf-8") as f:
    text = f.read()

text = re.sub(r"(<!--AGE(?:_ES)?-->)\d+(<!--/AGE(?:_ES)?-->)", rf"\g<1>{age}\g<2>", text)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(text)
