def reverseVowels(s: str) -> str:
    chars = "eaiouEAIOU"
    left = 0
    right = len(s) - 1
    s = list(s)
    while left <= right:
        if left >= right:
            break
        if s[left] not in chars:
            left += 1
        if s[right] not in chars:
            right -= 1
        if s[left] in chars and s[right] in chars:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return "".join(s)
