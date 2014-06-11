import math

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = float('-inf')
    max_left = 0
    max_right = 0
    total = 0
    for i in range(mid, low - 1, -1):
        total += A[i]
        if (total > left_sum):
            left_sum = total
            max_left = i
    right_sum = float('-inf')
    total = 0
    for j in range(mid + 1, high + 1):
        total += A[j]
        if (total > right_sum):
            right_sum = total
            max_right = j

    return (max_left, max_right, left_sum + right_sum)



def find_maximum_subarray(A, low, high):
    if (high == low):
        return (low, high, A[low])
    else:
        mid = math.floor((low + high)/2)
        (left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)

        if ((left_sum >= right_sum) and (left_sum >= cross_sum)):
            return (left_low, left_high, left_sum)
        elif ((right_sum >= left_sum) and (right_sum >= cross_sum)):
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)




def brute_force_max_subarray(A):
    total = float('-inf')
    left = 0
    right = 0
    for i in range(0, len(A) - 1):
        current_total = A[i]
        if current_total > total:
            total = current_total
        for j in range(i + 1, len(A)):
            current_total += A[j]
            if current_total > total:
                total = current_total
                left = i
                right = j
    return(total, left, right)



def linear_max_subarray(A):
    total = float('-inf')
    left = 0
    right = 0
    current_total = 0
    for i in range(0, len(A)):
        current_total += A[i]
        if current_total > total:
            total = current_total
            right = i
        else:
            left = right = i
            
    return(sum(A[left + 1:right + 1]), left + 1, right)







        

    

    




