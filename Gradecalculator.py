M = int(input("Enter maths marks here:"))
E = int(input("Enter english marks here:"))
S = int(input("Enter science marks here:"))

Total_Marks = M+E+S
Average_Marks = Total_Marks/3

Percentage =(Total_Marks/300)*100

grade = ""

if Percentage >90:
    grade ="A"
elif Percentage > 80 and Total_Marks <=90:
    grade ="B"
elif Percentage > 70 and Total_Marks <=80:
    grade = "C"
else:
    grade = "D"

print(f"Total marks:{Total_Marks}\nAverage marks:{Average_Marks}\nGrade:{grade}")