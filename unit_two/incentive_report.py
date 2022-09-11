# We will import pretty print to view our out output in pretty way.
from pprint import pprint

# Employee evaluation data
employee_eva = {
        "emp1": ["shalaby",2000, "A"],
        "emp2": ["ali",2000, "B"],
        "emp3": ["abeer",1000, "C"],
        "emp4": ["sameh",2500, "A"],
        "emp5": ["abd Allah",1500, "C"],
        "emp6": ["fatemah",1000, "B"],
        "emp7": ["jehad",700, "C"],
        "emp8": ["mahmood",500, "A"],         
        "emp9": ["rola",1200, "C"],
        "emp10": ["noor",1800, "B"],
        }
# Print the report befor modify it
print("The Incentive Report befor modify it.\n\n")
print("_"*34)
pprint(employee_eva)
# search for the Employee and modify their salary from their mark

for emp_num, data in employee_eva.items():
    if "B" in data:
        continue
    elif "A" in data:
        data[1] = data[1] + 100
    else:
        data[1] = data[1] - 100
else:
    print("_"*34)
    print("\n\nThe Incentive Report after modify it.\n\n")
    pprint(employee_eva)
    print("\n\n--> Send this report to acountant <--")
