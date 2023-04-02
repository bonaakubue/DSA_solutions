#Write a pseudo-code description of a function that reverses a list of n integers, 
# so that the numbers are listed in the opposite order than they were before, 
# and compare this method to an equivalent Python function for doing the same thing.

#Pseudocode

#Step 1 - define a new empty list
#Step 2 - loop through the items in the list starting from the last item
#Step 3 - append the items to the new list

nums = [1,2,3,4,5]

new_list = []

count = len(nums) - 1

for num in nums:
    item = nums[count]
    new_list.append(item)
    count-=1

print(new_list)

#using built-in method reverse()
nums.reverse()

print(nums)