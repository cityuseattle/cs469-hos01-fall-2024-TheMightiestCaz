def binarySearch(arr, target):
    #initialize the lower bound and upper bound
    low, high = 0, len(arr)-1
    while low <= high:
        #check the middle element
        mid = (low + high) // 2
        guess = arr[mid]
        #Found the target.
        if guess == target:
            return mid
        if guess > target:
            high = mid -1
        else:
            low = mid + 1
    return None

#Test case 1
input = [1, 3, 5, 9, 10, 11]
target = 3
print(binarySearch(input, target))

#Test case 2
input = ["Apple", "Banana", "Cherries", "Grapes", "Orange"]
target = "Grapes"
print(binarySearch(input, target))