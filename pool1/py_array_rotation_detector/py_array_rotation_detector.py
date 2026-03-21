def array_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:
    j = 0
    i = 0
    if len(arr1) != len(arr2):
        return False
    if sorted(arr1) != sorted(arr2):
        return False
    if arr1 == arr2:
        return True
    while arr1[i] != arr2[j]:
        j += 1
    for i in range(0, len(arr1) - 1):
        if j > len(arr1) - 1:
            j = 0
        if arr1[i] != arr2[j]:
            return False
        j += 1
    return True

# print(array_rotation_detector([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])) #True
# print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3])) #True
# print(array_rotation_detector([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])) #True
# print(array_rotation_detector([1, 2, 3, 4, 5], [2, 3, 4, 5, 1])) #True
# print(array_rotation_detector([1, 2, 3], [1, 3, 2])) #False
# print(array_rotation_detector([1, 2, 3], [1, 2])) #False
# print(array_rotation_detector([], [])) #True
# print(array_rotation_detector([1, 1, 1], [1, 1, 1])) #True
# print(array_rotation_detector([1, 1, 1], [11111111])) #False