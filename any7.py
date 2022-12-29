def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE
    counter = 0 
    for num in nums:
        if num == 7:
            counter += 1
    if counter >= 1:
        return True
    else:
        return False            
print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

