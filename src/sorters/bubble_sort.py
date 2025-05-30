from typing import Literal


def bubble_while(nums: list[int], order: Literal['asc', 'desc']):
    size = len(nums)

    i = 0

    while i < size:
        j = i
        is_sorted = True
        while j < size - 1:
            if nums[j] > nums[j + 1]:
                is_sorted = False
                temp_current = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp_current

            j += 1
        if is_sorted:
            print('ordered with while: ', nums)
            return nums
        i += 1

    return nums


def bubble(nums: list[int], order: Literal['asc', 'desc']):
    size = len(nums)

    for _ in nums:
        is_sorted = True

        print('current nums: ', nums)

        for i in range(size - 1):
            if order == 'desc':
                if nums[i] < nums[i + 1]:
                    print(f'{nums[i]} is smaller than {nums[i+1]}. Changing')
                    is_sorted = False
                    # nums[i + 1], nums[i] = nums[i], nums[i + 1]
                    temp_current = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = temp_current
            elif order == 'asc':
                if nums[i] > nums[i + 1]:
                    print(f'{nums[i]} is greater than {nums[i+1]}. Changing')
                    is_sorted = False

                    temp_current = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = temp_current

        if is_sorted:
            print('nums sorted. \n')
            return
    return nums


bubble([5, 1, 3, 10, 4], 'desc')
bubble_while([545, 2, 6], 'asc')
