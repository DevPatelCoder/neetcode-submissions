class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1

            max_frequency = max(max_frequency, count[s[right]])

            window_length = right - left + 1
            replacements = window_length - max_frequency

            while replacements > k:
                count[s[left]] -= 1
                left += 1

                window_length = right - left + 1
                replacements = window_length - max_frequency

            max_length = max(max_length, window_length)

        return max_length