# stolen
# https://leetcode.com/problems/validate-stack-sequences/solution/

def validate_pushed_popped(pushed: list, popped: list) -> bool:
    if len(pushed) != len(popped):
        return False
    j = 0
    stack = []
    for x in pushed:
        stack.append(x)
        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j += 1

    return j == len(popped)


def solution():
    pushed = list(map(int, input().split()))
    popped = list(map(int, input().split()))
    result = validate_pushed_popped(pushed, popped)
    print(result)


solution()
