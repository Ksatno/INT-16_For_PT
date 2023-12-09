import re

def title1(input: str) -> str:
    result = re.sub(r"(\w)(\w*)", lambda m: m.group(1).upper() + m.group(2).lower(), input)
    return result

def title2(input: str) -> str:
    capitalizeNext = True
    result = ""
    for char in input:
        if char.isalpha():
            if capitalizeNext:
                result += char.upper()
                capitalizeNext = False
            else:
                result += char.lower()
        else:
            result += char
            if char.isspace():
                capitalizeNext = True
    return result

def title3(input: str) -> str:
    prevIsLetter = False
    result = ""
    for char in input:
        if char.isalpha():
            if prevIsLetter == False:
                result += char.upper()
            else:
                result += char.lower()
            prevIsLetter = True
        else:
            result += char
            prevIsLetter = False
    return result


if __name__ == "__main__":
    inputString1 = "тесТОвое задание     для  pt"
    print(title1(inputString1))
    inputString2 = "тесТОвое заДаНиE     для  pt, мною    ,     быЛо          РешеНо"
    print(title2(inputString2))
    inputString3 = "и    это Замечательно    !   "
    print(title3(inputString3))
