import sys
import math

input = sys.stdin.readline

def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def closest_pair(px, py):
    n = len(px)
    if n <= 3:
        min_dist = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                min_dist = min(min_dist, dist(px[i], px[j]))
        return min_dist

    mid = n // 2
    mid_x = px[mid][0]
    Qx = px[:mid]
    Rx = px[mid:]

    midpoint = px[mid][0]
    Qy = []
    Ry = []
    for point in py:
        if point[0] <= midpoint:
            Qy.append(point)
        else:
            Ry.append(point)

    d1 = closest_pair(Qx, Qy)
    d2 = closest_pair(Rx, Ry)
    d = min(d1, d2)

    # Verifica cruzamento
    strip = [p for p in py if abs(p[0] - mid_x) < d]
    for i in range(len(strip)):
        for j in range(i+1, min(i+7, len(strip))):  # até 7 pontos seguintes
            d = min(d, dist(strip[i], strip[j]))

    return d

while True:
    line = input()
    if not line:
        break
    n = int(line.strip())
    if n == 0:
        break

    points = []
    for _ in range(n):
        x, y = map(float, input().split())
        points.append((x, y))

    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    answer = closest_pair(px, py)

    if answer >= 10000:
        print("INFINITY")
    else:
        print(f"{answer:.4f}")