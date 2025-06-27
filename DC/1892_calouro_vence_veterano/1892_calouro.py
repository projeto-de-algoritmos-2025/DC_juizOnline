def merge_sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, inv_left = merge_sort_and_count(arr[:mid])
    right, inv_right = merge_sort_and_count(arr[mid:])
    
    merged, inv_split = merge_and_count(left, right)
    return merged, inv_left + inv_right + inv_split

def merge_and_count(left, right):
    merged = []
    count = 0
    i = j = 0
    n_left = len(left)
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += n_left - i  # todos os restantes em left são > right[j]
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, count

# Leitura dos casos de teste
while True:
    try:
        N = int(input())
        matriculas = [input().strip() for _ in range(N)]
        _, inversoes = merge_sort_and_count(matriculas)
        print(inversoes)
    except EOFError:
        break