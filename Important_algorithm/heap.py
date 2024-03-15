# %%
import math
class Heap(list):
  def __init__(self, arr = [], heap_size = math.inf):
    super().__init__(arr)
    self.heap_size = min(heap_size, len(self))

  PARENT = lambda i : (i - 1) // 2 # index of parent
  LEFT = lambda i : 2 * i + 1 # index of left child
  RIGHT = lambda i : 2 * i + 2 # index of right child

  @staticmethod
  def is_max_heap(h, i = 0):
    if i >= h.heap_size - 1:
      return True

    l, r = Heap.LEFT(i), Heap.RIGHT(i)

    if r < h.heap_size and h[r] > h[i]:
      return False
    elif l < h.heap_size and h[l] > h[i]:
      return False
    else:
      return h.is_max_heap(r) and h.is_max_heap(l)

  @staticmethod
  def max_heapify(h, i = 0):
    l, r = Heap.LEFT(i), Heap.RIGHT(i)

    if l < h.heap_size and h[l] > h[i]:
      largest = l
    else:
      largest = i

    if r < h.heap_size and h[r] > h[largest]:
      largest = r

    if largest != i:
      h[i], h[largest] = h[largest], h[i]
      h.max_heapify(h, largest)

  @staticmethod
  def build_max_heap(arr):
    h = Heap(arr) # this sets heap_size = len(arr)
    n = h.heap_size

    for i in range(n // 2 - 1, 0, -1):
      h.max_heapify(h, i)
    
  @staticmethod
  def heap_sort(arr):
    Heap.build_max_heap(arr)
    h = Heap(arr)
    n = h.heap_size

    for i in range(n - 1, 1, -1):
      arr[0], arr[i] = arr[i], arr[0]
      h.heap_size = h.heap_size - 1
      Heap.max_heapify(h, 0)

# %%
