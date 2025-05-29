from typing import Literal


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


bubble([5, 1, 3, 10, 4], 'desc')


bubble([85, 2, 1, 0, 4], 'asc')
