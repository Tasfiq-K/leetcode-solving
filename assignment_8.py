from collections import Counter

class Solution:
    """
    A solution class
    """
    def SingleElement(self, nums: list) -> int:
        """
        Finds that one element who is single. :p

        Args: 
            nums: [list] : A list containing numbers
        Returns: returns the index element who is single
        """

        counter_dict = Counter(nums)

        for key, value in counter_dict.items():
            # check if the value occurs only one for then return the corresponding key
            # else return None
            if value == 1:
                return key
        return None

sol = Solution()
res = sol.SingleElement([3, 3, 1, 1, 1, 4, 4, 5])
print(res)