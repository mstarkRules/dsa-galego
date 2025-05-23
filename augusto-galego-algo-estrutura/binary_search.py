def binary_search(nums, n):
    low = 0
    high = len(nums)
    steps = 0

    while low < high:
        steps += 1

        mid = int((low + high) / 2)
        print("step: ", steps)
        print("low: ", low)
        print("high: ", high)
        print("mid: ", mid)

        if (nums[mid] == n):
            print("step: ", steps)
            print("low: ", low)
            print("high: ", high)
            print("mid: ", mid)
            print("founded at mid: ", mid)
            print("founded: ", nums[mid])

            return mid
        elif nums[mid] < n:
            print("it is in the right side. Mid number:", nums[mid])
            low = mid + 1
        else:
            # comment
            print("it is in the left side. Mid number::", nums[mid])
            high = mid
    return -1


a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
     13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]


binary_search(d, 3)
