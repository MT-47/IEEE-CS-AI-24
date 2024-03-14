from typing import List

class Solution:
    def sampleStats(self) -> List[float]:
        try:
            count_input = input("Enter the count list separated by spaces: ")
            count = list(map(int, count_input.split()))

            # Check count exactly 256 elements
            if len(count) != 256:
                raise ValueError("Input list must contain exactly 256 elements")

            # Check for non-negative integers
            if any(not isinstance(x, int) or x < 0 for x in count):
                raise ValueError("All elements in the input list must be non-negative integers")

        except ValueError as ve:
            print("Input Error:", ve)
            return []

        def minimum():
            for i in range(len(count)):
                if count[i] > 0:
                    return i
            return 0  # If all elements are zero, return 0 as minimum

        def maximum():
            for i in reversed(range(len(count))):
                if count[i] > 0:
                    return i
            return 255  # If all elements are zero, return 255 as maximum
        
        def mean():
            total_sum = sum(i * count[i] for i in range(len(count)))
            total_count = sum(count)
            if total_count == 0:  # If total count is zero, return 0 as mean
                return 0
            mean = total_sum / total_count
            return mean
        
        def median():
            total_count = sum(count)
            if total_count == 0:  # If total count is zero, return 0 as median
                return 0
            
            count_sum = 0
            median1, median2 = None, None
            for i, c in enumerate(count):
                count_sum += c
                if median1 is None and count_sum >= total_count // 2:
                    median1 = i
                if count_sum >= total_count // 2 + 1:
                    median2 = i
                    break
            if total_count % 2 == 1:
                return median2
            else:
                return (median1 + median2) / 2
        
        def mode():
            if all(x == 0 for x in count):  # If all elements are zero, return 0 as mode
                return 0
            mode = count.index(max(count))
            return mode

        return [minimum(), maximum(), mean(), median(), mode()]

solution = Solution()
print(solution.sampleStats())