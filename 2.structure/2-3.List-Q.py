from collections import deque

queue = deque()
queue.append(1) # 요소 add
queue.append(2)
first_item = queue.popleft() # 첫 번째 요소 제거 1 제거
print(queue) # deque([2])