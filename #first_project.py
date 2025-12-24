#first project 
#stage 1 - Student Performance Analyzer

total=0
marks=[]

std_Name=input("Enter Student Name:")

for i in range(1,6,):
    mark=float(input(f"Enter marks for subject {i}:"))
    marks.append(mark)
    total+=mark

average=total/5

if average>=90:
    grade="S"
elif average>=80:
    grade="A+"
elif average>=70:
    grade="A"
elif average>=60:
    grade="B+"
elif average>=55:
    grade="B"
elif average>=50:
    grade="C"
elif average>=45:
    grade="P"
else:
    grade="F"

print("\n--- student Performance---")
print(f"\nstudent Name: {std_Name}")
print(f"Total Marks: {total}")
print(f"Average Marks : {average:.2f}")
print(f"Grade {grade}")