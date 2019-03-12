'''
Grading PROGRAM
---------------
Create a program that asks the user for their semester grade, final exam grade,
and final exam worth and then calculates the overall final grade.
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''
sem_grade=int(input("Enter semester grade:"))
final_exam=int(input("Enter final exam grade:"))
exam_worth=int(input("Enter exam worth:"))
overall_grade=sem_grade*(1-exam_worth/100)+(final_exam*exam_worth/100)
print("Overall:", overall_grade)
if overall_grade>90:
    print("A")
elif overall_grade>80:
    print("B")
elif overall_grade>70:
    print("C")
elif overall_grade>60:
    print("D")
else:
    print("Transfer to Johnston!")