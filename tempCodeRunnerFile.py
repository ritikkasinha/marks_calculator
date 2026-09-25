print("Student Grade Calculator")
name = input("Enter student name: ")
m1 = int(input("Enter Python marks: "))
m2 = int(input("Enter Maths marks: "))
m3 = int(input("Enter English marks: "))
total = m1 + m2 + m3
average = total / 3
print("\nStudent:", name)
print("Total:", total)
print("Average:", average)
if average >= 90:
    print("Grade: A+")
elif average >= 80:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 50:
    print("Grade: D")
else:
    print("Grade: F")

if average >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")