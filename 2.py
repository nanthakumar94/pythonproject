# Balance and Unbalance problem
open_list = ["{", "[", "("]
close_list = ["}", "]", ")"]


def check_balance(str):
    stack = []
    for i in str:
        if i in open_list:
            stack.append(i)
        if i in close_list:
            pos = close_list.index(i)
            if len(stack) > 0 or open_list[pos] == i:
                stack.pop()
    if len(stack) == 0:
        return "Balance"
    else:
        return "Unbalance"


print(check_balance("[]{([)}"))
