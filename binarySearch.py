# Binary search using python

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index

        # Check if the middle element is equal to the target
        if arr[mid] == target:
            return mid
        # If the target is less than the middle element, search the left half
        elif arr[mid] > target:
            right = mid - 1
        # If the target is greater than the middle element, search the right half
        else:
            left = mid + 1

    return -1  # Return -1 if the target is not found in the array

# Example usage:
arr = [11, 12, 22, 25, 34, 64, 90]
target = 25
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
