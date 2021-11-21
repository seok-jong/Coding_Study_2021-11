import sys
sys.stdin=open("input.txt", "r")

def Count(len):
  cnt = 1
  ep = gap[0]
  for i in range(1, n):
    if gap[i] - ep >= len:
      cnt += 1
      ep = gap[i]
  return cnt

n, c = map(int, input().split())
gap = []
largest = 0

for i in range(n):
  tmp = int(input())
  gap.append(tmp)
  largest = max(largest, tmp)

gap.sort()

lt = 1
rt = largest

while lt <= rt:
  mid = (lt+rt) // 2
  if Count(mid) >= c:
    res = mid
    lt = mid + 1
  else:
    rt = mid - 1

print(res)






  
      




