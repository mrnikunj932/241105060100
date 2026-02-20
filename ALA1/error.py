print("Voting Eligibility System")
people = int(input("Enter number of people: "))
i = 0
eligible = 0
not_eligible = 0
while i < people:
age = int(input("Enter age: "))
if age >= 18:
eligible = eligible + 1
print("Eligible")
else:
not_eligible = not_eligible + 1
print("Not Eligible"
i = i + 1
print("Eligible count:", eligible)
print("Not Eligible count:", not_eligible)
if eligible > not_eligible:

print("Majority eligible")
else:
print("Majority not eligible")

