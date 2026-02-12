# Permuate a list using backtracking
def permute(nums):
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  # Swap
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # Backtrack

    result = []
    backtrack(0)
    return result

# Generate combinations of k elements from a list using backtracking
def combine(nums, k):
    result = []
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # Backtrack

    backtrack(0, [])
    return result

# Test cases
if __name__ == "__main__":
    nums = [1, 2, 3]
    print("Permutations of", nums, ":", permute(nums))

    k = 2
    print("Combinations of", nums, "taken", k, "at a time:", combine(nums, k))