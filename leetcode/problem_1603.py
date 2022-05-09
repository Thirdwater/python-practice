"""A solution to leetcode problem 1603
https://leetcode.com/problems/design-parking-system/
"""
from enum import Enum


class Size(Enum):
    BIG = 1
    MEDIUM = 2
    SMALL = 3


class ParkingSystem:
    """
    Cars can only park on their corresponding slot size.
    (Smaller cars cannot park in bigger slot sizes)
    """

    def __init__(self, big: int, medium: int, small: int):
        self.max_parking_spaces = {
            Size.BIG.value: big,
            Size.MEDIUM.value: medium,
            Size.SMALL.value: small,
        }
        self.num_parked_cars = {
            Size.BIG.value: 0,
            Size.MEDIUM.value: 0,
            Size.SMALL.value: 0,
        }

    def addCar(self, carType: int) -> bool:
        # We should ideally be using the enum type instead of int.
        # This signature is just from the prompt.
        if self.num_parked_cars[carType] >= self.max_parking_spaces[carType]:
            return False
        
        self.num_parked_cars[carType] += 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
