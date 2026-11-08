class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}
        have = 0
        required = len(need)

        left = 0
        best_length = float("inf")
        best_start = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == required:
                current_length = right - left + 1

                if current_length < best_length:
                    best_length = current_length
                    best_start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_start:best_start + best_length]