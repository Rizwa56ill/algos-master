"""
Bubble Sort Algorithm Implementation
"""

def bubble_sort(arr):
    """
    Sort an array using bubble sort algorithm.
    
    Args:
        arr: List of comparable elements to sort
        
    Returns:
        Sorted list in ascending order
    """
    if not arr:
        return arr
    
    n = len(arr)
    result = arr.copy()
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        
        if not swapped:
            break
    
    return result
