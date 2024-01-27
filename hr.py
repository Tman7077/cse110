hr_dict = {}
with open('hr_system.txt') as f:
     for line in f:
          line = line.strip()
          emp_list = line.split(" ")
          emp_id = emp_list[1]; emp_list.pop(1)
          emp_list[2] = int(emp_list[2])
          hr_dict.update({emp_id:emp_list})

for eid in hr_dict.keys():
     e = hr_dict[eid]
     pay = e[2] / 24
     if e[1] == 'Engineer':
          pay += 1000
     print(f'{e[0]} (ID: {eid}), {e[1]} - ${pay:.2f}')