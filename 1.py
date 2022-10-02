# input = "[]{}" True
# input = "{](" False

def is_valid(str):
    stack = []
    pchar = {"[": "]", "(": ")", "{": "}"}
    for i in str:
        if i in pchar:
            stack.append(i)
        elif len(stack) == 0 or pchar[stack.pop()] != i:
            return False
    return len(stack) == 0


print(is_valid("[]{}"))
