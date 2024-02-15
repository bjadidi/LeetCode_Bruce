
def solution(nums):
    list_nums = nums
    for item in list_nums:
        max_num = max(list_nums)
        list_nums.remove(max_num)

        if sum(list_nums) > max_num and len(list_nums)>1:
            return (sum(list_nums)+(max_num))
        
    return -1
   

nums = [1,2,3,4,5]