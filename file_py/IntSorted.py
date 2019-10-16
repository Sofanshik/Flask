import time

print(time.process_time())

#THERT SORT
def part(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def q_sort(nums):
    def _q_sort(items, low, high):
        if low < high:
            split_index = part(items, low, high)
            _q_sort(items, low, split_index)
            _q_sort(items, split_index + 1, high)

    _q_sort(nums, 0, len(nums) - 1)

    return nums
