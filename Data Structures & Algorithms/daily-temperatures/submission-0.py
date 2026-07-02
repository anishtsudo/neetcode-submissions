class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Answer array, initialized with 0s
        res = [0] * len(temperatures)

        # Stack stores indices (days), NOT temperatures
        stack = []

        # Go through each day
        for i in range(len(temperatures)):

            # While current day is warmer than the day on top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prevDay = stack.pop()          # Day that just found a warmer day
                res[prevDay] = i - prevDay     # Number of days waited

            # Current day is still waiting for a warmer future day
            stack.append(i)

        return res