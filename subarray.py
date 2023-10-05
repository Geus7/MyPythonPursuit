target = int(input("Enter the target sum: "))
nums = list(map(int, input("Enter a list of positive integers separated by spaces: ").split()))
left = 0 
right = 0  
min_length = float('inf') 
current_sum = 0 

while right < len(nums):
    current_sum += nums[right]
    
    while current_sum >= target:
        min_length = min(min_length, right - left + 1)
        current_sum -= nums[left]
        left += 1
    right += 1
if min_length != float('inf'):
    print(f"The minimal subarray length with a sum >= {target} is {min_length}.")
else:
    print("No subarray found with a sum >= target.")
