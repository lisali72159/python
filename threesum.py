# Find sets of three numbers that add up to 0. No duplicates.
#  [ -1, 0, 1, 2, 1 -4] => [[-1,0,1],[-1,-1,2]]

def threesum(arr):
    arr.sort()
    answer = set()

    for idx, ele in enumerate(arr):
        start = idx + 1
        end = len(arr) - 1

        while start < end:
            print(ele) 
            print(arr)
            print(start)
            print(end)
            start += 1
            if -(ele) == arr[start] + arr[end]:
                answer.add([tuple([ele, arr[start], arr[end]])

            # if ele + arr[start] + arr[end] <= 0:
            #     start += 1

            # else:
            #     end -= 1
    return answer

print threesum([ -1, 0, 1, 2, 1 -4])


