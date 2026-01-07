# Write a function that takes an array and returns it reversed

# def reversing_array(arr):
#     left=0
#     right=len(arr)-1
#     while left<right:
#         arr[left],arr[right]=arr[right],arr[left]
#         left+=1
#         right-=1
#     return arr

# print(reversing_array([1,4,2,7,3,8]))


# Write a function that takes a list of numbers and returns the maximum

# def find_maximum(arr):
#     n=len(arr)
#     largest=arr[0]
#     for i in range(1,n):
#         if arr[i]>largest:
#             largest=arr[i]
#     return largest

# print(find_maximum([1,4,2,7,3,8]))

# write a function to reverse sort the array

def reverse_sorting(arr):
    # n=len(arr)
    # for i in range(n):
    #     for j in range(n-1-i):
    #         print("j",arr[j])
    #         print("j+1",arr[j+1])
    #         if arr[j]<arr[j+1]:
    #             arr[j],arr[j+1]=arr[j+1],arr[j]

    n=len(arr)
    x=arr[0]
    key=n//2
    for i in range(n):
        if x<arr[key]:
            x,arr[key]=arr[key],x
        key=key//2
    return arr
        
print(reverse_sorting([1,4,2,7,3,8]))
