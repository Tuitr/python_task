def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    nums_map = {}
    for i in range(len(nums)):
        if nums[i] in nums_map and abs(nums_map[nums[i]] - i) <= k:
            return True

        nums_map[nums[i]] = i
    return False
