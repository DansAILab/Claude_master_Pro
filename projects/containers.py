ages = {"Sam": 7, "Alex": 9}
print(ages["Sam"])


ages["Jordan"] = 12
ages["Sam"] = 8
for name in ages:
    print(name, "is", ages[name], "years old")