def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def bubble_sort(arr):
    n = len(arr)
    res = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res

# 示例
if __name__ == "__main__":
    import time
    nums = [5, 3, 8, 4, 2, 7, 1, 10]
    print("排序前：", nums)
    sorted_nums = quick_sort(nums)
    print("快速排序后：", sorted_nums)
    sorted_nums_bubble = bubble_sort(nums)
    print("冒泡排序后：", sorted_nums_bubble)

    # 比较两种排序的速度
    import random
    test_arr = [random.randint(0, 10000) for _ in range(1000)]
    t1 = time.time()
    quick_sort(test_arr)
    t2 = time.time()
    bubble_sort(test_arr)
    t3 = time.time()
    print(f"快速排序耗时: {t2 - t1:.6f} 秒")
    print(f"冒泡排序耗时: {t3 - t2:.6f} 秒")