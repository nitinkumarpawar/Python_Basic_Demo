import re

str_va = "1, Nitin, Pawar, 1234567891, 9152989989"

mobile_num = re.search("[0-9]{10,10}", str_va)
print(mobile_num)
mobile_all = re.findall("[0-9]{10,10}", str_va)
print(mobile_all)
