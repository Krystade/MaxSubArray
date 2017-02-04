def maxSequence(numbers):
    max = 0
    list = (0)
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if sum(numbers[i:j + 1]) > max:
                max = sum(numbers[i:j + 1])
                list = numbers[i:j + 1]
    return (max)

numbers = [-28, 28, 19, 8, -1, -22, -30, 5, 20, -15, 22, 2, 27, -19, -10, -28, -15, 2, 3, -25, 1, 20, -20, 27, -30, 9, 10, 25, -5, 12, -1, -22, -9, -21, -9, -2, 26, -13, -22, 30, 27, 27, -10, 15, 27, 25, 13, 19, -1, 27]
maxSequence(numbers)
#https://www.codewars.com/kata/maximum-subarray-sum/train/python
