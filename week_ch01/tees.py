student_id = 1000
student_name = "Liam"
subject = ["python", "stats", "mathmatics"]
score = 3.4
teacher = ("lee", "park")

print(f"학번이 {student_id}인 {student_id}은 {subject}과목을 수강하였고, 학점이 {score}이다.")
print(type(student_id), type(student_name), type(subject), type(score), type(True), type(False), type(teacher))
print(id(student_id), id(student_name), id(subject), id(score))