"""A solution to leetcode problem 1108
https://leetcode.com/problems/defanging-an-ip-address/
"""
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
