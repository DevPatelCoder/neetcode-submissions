class Solution:
    def longestPalindrome(self, s: str) -> str:

        if s == "":
            return ""

        # Add # between every character
        # Example: "abba" -> "^#a#b#b#a#$"
        transformed = "^#" + "#".join(s) + "#$"

        n = len(transformed)

        # palindrome_radius[i] tells us how far the
        # palindrome expands around position i
        palindrome_radius = [0] * n

        # Center and right boundary of the palindrome
        # that currently reaches the farthest right
        current_center = 0
        right_boundary = 0

        for i in range(1, n - 1):

            # Find the mirror position of i
            mirror_index = 2 * current_center - i

            # If i is inside the current palindrome,
            # reuse information from its mirror
            if i < right_boundary:
                palindrome_radius[i] = min(
                    palindrome_radius[mirror_index],
                    right_boundary - i
                )

            # Try to expand the palindrome around i
            while (
                transformed[i + palindrome_radius[i] + 1]
                == transformed[i - palindrome_radius[i] - 1]
            ):
                palindrome_radius[i] += 1

            # If this palindrome reaches farther right,
            # update the current center and boundary
            if i + palindrome_radius[i] > right_boundary:
                current_center = i
                right_boundary = i + palindrome_radius[i]

        # Find the palindrome with the largest radius
        best_center = 0
        best_radius = 0

        for i in range(n):
            if palindrome_radius[i] > best_radius:
                best_radius = palindrome_radius[i]
                best_center = i

        # Extract the palindrome from transformed string
        start = best_center - best_radius
        end = best_center + best_radius + 1

        longest_palindrome = transformed[start:end]

        # Remove the # characters
        longest_palindrome = longest_palindrome.replace("#", "")

        return longest_palindrome