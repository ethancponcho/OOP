import StudentClass as s


student = s.Student()

student.calc_age()
student.determine_register_date()

print(f"Student ID: {student.get_studentid}\nName: {student.get_name()}\nAge: {student.get_age()}\nClass: {student.get_class()}")

print("You can register from", student.get_register_date())
    