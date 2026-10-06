def canJump(nums: list[int]) -> bool:
    max_jump = 0
    for num in range(len(nums)):
        if num > max_jump:
            return False

        max_jump = max(max_jump, num + nums[num])

        if max_jump >= len(nums) - 1:
            return True
    return False
