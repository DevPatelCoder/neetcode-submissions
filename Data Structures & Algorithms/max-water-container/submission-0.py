class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        max_volume = 0
        while left < right:
            if height[left]>height[right]:
                volume = height[right]*(right-left)
                if volume>max_volume:
                    max_volume = volume
                right-=1

            elif height[left]<height[right]:
                volume = height[left] * (right - left)
                if volume > max_volume:
                    max_volume = volume
                left+=1

            else:
                volume = height[left] * (right - left)
                if volume > max_volume:
                    max_volume = volume
                left += 1
        return max_volume