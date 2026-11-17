import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        if self.right and -self.left[0] > self.right[0]:
            value = -heapq.heappop(self.left)
            heapq.heappush(self.right, value)

        if len(self.left) > len(self.right) + 1:
            value = -heapq.heappop(self.left)
            heapq.heappush(self.right, value)

        if len(self.right) > len(self.left):
            value = heapq.heappop(self.right)
            heapq.heappush(self.left, -value)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]

        return (-self.left[0] + self.right[0]) / 2
        
        