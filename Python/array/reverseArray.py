
## D.Dtructure
def reverseNumber(nums):
    start_index = 0
    end_index = len(nums) -1

    while end_index > start_index:
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index = start_index + 1
        end_index = end_index - 1

if __name__ == '__main__':
    n = [24,12,2,4]
    reverseNumber(n)
    print(n)

##Slicing
# arr = [10,20,45,56]
# nums = arr[::-1] ## reversing
# print ("Result - ", nums)

## reverse 
# arr = [2,3,4,5,6]
# arr.reverse()
# print("Reverse array - ", arr)

##reversed
# arr = [2,3,4,5,6,7]
# nums = list(reversed(arr))
# print(nums)
