"""A solution to leetcode problem 1828
https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
"""
import math
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        points_in_circle = []
        for circle in queries:
            x, y, radius = circle
            circle_center = [x, y]
            num_points = 0
            for point in points:
                if self.distanceBetween(point, circle_center) <= radius:
                    num_points += 1
            points_in_circle.append(num_points)
        return points_in_circle

    def distanceBetween(self, point1: List[int], point2: List[int]) -> int:
        x1, y1 = point1
        x2, y2 = point2
        return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
