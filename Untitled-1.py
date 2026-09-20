print("=====STUDENTS ATTENDENCEVV=====")
print("TOTAL NUMBER OF WORKING DAYS=90")
workingdays=90

STUDENTS=int(input("ENTER THE STUDENTS (1:5):"))
for i in range(STUDENTS):
  NAMES=input("ENTER THE STUDENT NAME:")
  ATTENDENCE=int(input("ENTER NO OF DAYS PRESENT:"))
  PERCENTAGE=(ATTENDENCE/workingdays)*100 
  print(f"ATTENDENCE PECENTAGE of {NAMES}={PERCENTAGE:.2f}%")
  print("-----------------")