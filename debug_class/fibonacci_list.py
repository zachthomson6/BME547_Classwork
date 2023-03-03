"""
Create a list that contains each step in the Fibonacci Sequence:
[
  [0, 1],
  [0, 1, 1],
  [0, 1, 1, 2],
  [0, 1, 1, 2, 3],
  [0, 1, 1, 2, 3, 5],
  [0, 1, 1, 2, 3, 5, 8]
  [0, 1, 1, 2, 3, 5, 8, 13]
]
"""

overall_list = list()
working_list = [0, 1]
overall_list.append(working_list)

for i in range(6):
    new_entry = working_list[-2] + working_list[-1]
    working_list.append(new_entry)
    overall_list.append(working_list)

print("Result: {}".format(overall_list))
for item in overall_list:
    print(item)
