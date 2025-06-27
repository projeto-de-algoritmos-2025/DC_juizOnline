def max_subarray_divide_and_conquer(arr, l, r):
    if l > r:
        return 0
    if l == r:
        return max(0, arr[l])

    mid = (l + r) // 2

    left_max = max_subarray_divide_and_conquer(arr, l, mid)
    right_max = max_subarray_divide_and_conquer(arr, mid + 1, r)

    left_sum = float('-inf')
    temp = 0
    for i in range(mid, l - 1, -1):
        temp += arr[i]
        left_sum = max(left_sum, temp)

    right_sum = float('-inf')
    temp = 0
    for i in range(mid + 1, r + 1):
        temp += arr[i]
        right_sum = max(right_sum, temp)

    cross_max = left_sum + right_sum

    return max(left_max, right_max, cross_max)

while True:
    try:
        N = int(input())
        cost = int(input())
        revenues = [int(input()) for _ in range(N)]
        profits = [r - cost for r in revenues]

        max_profit = max_subarray_divide_and_conquer(profits, 0, N - 1)
        print(max_profit)
    except EOFError:
        break
