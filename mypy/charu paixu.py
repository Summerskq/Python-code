def insert_sort(list):
    """插入排序"""
    n = len(list)
    for i in range(1, n):  # 未排序序列从第二个元素开始遍历
        for j in range(i, 0, -1):  # 已排序序列从后往前遍历
            if list[j] < list[j - 1]:  # 如果当前元素小于前一个元素, 则交换元素位置
                list[j], list[j - 1] = list[j - 1], list[j]
            else:  # 如果大于前一个元素, 则保持位置不变
                break


if __name__ == '__main__':
    list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("排序前:%s" % list1)
    insert_sort(list1)
    print("排序后:%s" % list1)

