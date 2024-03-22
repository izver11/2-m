def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Исходный неотсортированный список:", unsorted_list)


sorted_list = bubble_sort(unsorted_list.copy())
print("Отсортированный список (метод пузырьковой сортировки):", sorted_list)


target_element = 25
index = binary_search(sorted_list, target_element)
if index != -1:
    print(f"Элемент {target_element} найден по индексу {index} в отсортированном списке.")
else:
    print(f"Элемент {target_element} не найден в отсортированном списке.")
