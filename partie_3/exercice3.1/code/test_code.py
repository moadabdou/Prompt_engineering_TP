def calculate_average(numbers_list):
    # This function calculates the average of numbers in a list
    # It has some issues
    total = 0
    for num in numbers_list:
        total += num
    average = total / len(numbers_list)
    return average
# Example of usage (might cause errors)
my_nums = [1, 2, 'three', 4] # <-- Error here
avg = calculate_average(my_nums)
print(f"Average: {avg}")

"""
output
Traceback (most recent call last):
  File "C:\Users\dell\Desktop\cppPractice\prompt_tp\partie_3\exercice3.1\code\test_code.py", line 11, in <module>
    avg = calculate_average(my_nums)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\dell\Desktop\cppPractice\prompt_tp\partie_3\exercice3.1\code\test_code.py", line 6, in calculate_average
    total += num
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
"""