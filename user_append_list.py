def main():
     print("Enter a list of numbers. When you are finished, enter 0.")
     nums = []
     inp = -1
     while inp != 0:
          inp = int(input("Enter number: "))
          nums.append(inp)
     #
     sum = 0
     for i in nums:
          sum += i
     print(f'Sum: {sum}')
     #
     avg = sum / len(nums)
     print(f'Average: {avg}')
     #
     max_num = -2147483647
     for i in nums:
          if i > max_num:
               max_num = i
     print(f'Max: {max_num}')
     #
     min_pos = max_num + 1
     for i in nums:
          if i < min_pos and i > 0:
               min_pos = i
     print(f'Minimum positive: {min_pos}')
     #
     nums_copy = nums.copy()
     sorted_nums = []
     min_num = max_num
     print(f'Min: {min_num}')
     for _ in range(len(nums_copy)):
          for i in nums_copy:
               if i < min_num:
                    min_num = i
          sorted_nums.append(min_num)
          nums_copy.pop(nums_copy.index(min_num))
          min_num = max_num
     print(f'Sorted list: {sorted_nums}')

if __name__ == "__main__":
     main()