# Balance and Unbalance problem
open_list = ["{", "[", "("]
close_list = ["}", "]", ")"]

#add to check this
def check_balance(str):
    stack = []
    for i in str:
        #i for change
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
#this for local branch

print(check_balance("[]{([)}"))
