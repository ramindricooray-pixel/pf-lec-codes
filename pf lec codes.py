marks = []
failed_subjects = 0

for i in range(1, 7):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)
    if m < 50:
        failed_subjects += 1

total = sum(marks)
average = total / 6

print(f"\nTotal: {total}, Average: {average}")
print(f"Subjects below 50: {failed_subjects}")

if average >= 60 and failed_subjects == 0:
    print("Result: Excellent Performance")
elif average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
