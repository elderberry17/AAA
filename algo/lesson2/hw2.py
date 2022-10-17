# господи, победа:
# https://www.geeksforgeeks.org/the-stock-span-problem/

def calculate_stock_spans(prices: list) -> list:
    spans = [1]
    big_stack = [0]
    for i in range(1, len(prices)):
        while len(big_stack) > 0 and prices[big_stack[-1]] <= prices[i]:
            big_stack.pop()
        if len(big_stack) == 0:
            spans.append(i + 1)
        else:
            spans.append(i - big_stack[-1])
        big_stack.append(i)

    return spans


def solution():
    prices = list(map(int, input().split()))
    spans = calculate_stock_spans(prices)
    print(' '.join(map(str, spans)))


solution()
