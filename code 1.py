def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

def remove_duplicates_string(s):
    seen = set()
    result = ""
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result += ch
    return result

def largest_number(nums):
    return max(nums)

def second_largest(nums):
    unique_nums = sorted(set(nums))
    return unique_nums[-2] if len(unique_nums) >= 2 else None

def remove_duplicates_list(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def missing_number(nums, n):
    expected = n * (n + 1) // 2
    return expected - sum(nums)

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return None