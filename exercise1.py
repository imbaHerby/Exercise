class myClass:
    def __init__(self):
        pass

    def aboveBelow(self, nums: list, target: int) -> dict:
        countS = countL = 0

        for n in nums:
            if n > target:
                countL += 1
            elif n < target:
                countS += 1

        return {
            'above': countL,
            'below': countS,
        }

    def stringRotation(self, string: str, amount: int) -> str:
        if not string:
            return string

        # in case of overflowed
        amount %= len(string)

        return string[amount:] + string[:amount]


# test cases
instan = myClass()
print(instan.aboveBelow([], 6))
print(instan.aboveBelow([1, 5, 2, 1, 10], 6))
print(instan.stringRotation('', 6))
print(instan.stringRotation('123456', 1))
print(instan.stringRotation('123456', 3))
print(instan.stringRotation('123456', 6))
print(instan.stringRotation('123456', 8))
print(instan.stringRotation('123456', 61))
