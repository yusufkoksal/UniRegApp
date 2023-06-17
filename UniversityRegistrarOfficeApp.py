def add_new_course():
    course_name = input("Please enter the course name: ")
    instructor_name = input("Please enter instructor name:")
    course_code = input("Please enter the course code:")

    with open("courses.txt") as read_file:
        all_lines = read_file.readlines()
        found = False
        for line in all_lines:
            line_data = line.split(";")
            if line_data[0] == course_code:
                found = True
                print("The course already exists!!!")
                break
    if not found:
        with open("courses.txt", "a") as write_file:
            write_file.write(course_code + ";" + course_name + ";" + instructor_name + ";" + "0" + "\n")


def search_by_code():
    search_code = input("Please enter a code to looking for course:")

    with open("courses.txt", "r") as search_file:
        course_codes = search_file.readlines()
        found = False
        for line in course_codes:
            if search_code in line:
                found = True
                print(line)
                break
        if not found:
            print("Course does not exist")


def list_all_courses():
    with open("courses.txt", "r") as course_list_file:
        all_courses = course_list_file.readlines()
        for line in all_courses:
            print(line, end="")


def list_registered_courses():
    with open("courses.txt") as course_file:
        all_lines = course_file.readlines()
        for line in all_lines:
            course_data = line.split(";")
            if course_data[3] != "0\n":
                print(line)


def search_by_name():
    search_name = input("Please enter a name to looking for course:")

    with open("courses.txt", "r") as search_file:
        course_names = search_file.readlines()
        found = False
        for line in course_names:
            if search_name in line:
                found = True
                print(line)
        if not found:
            print("Course does not exist!!!")


def students_with_their_courses():
    with open("students.txt") as student_file:
        all_students_with_courses = student_file.readlines()
        for line in all_students_with_courses:
            student_data = line.split(";")
            print("ID:" + student_data[0] + "     Student Name:" + student_data[1] + "\n" + "***" + student_data[2])


def register_a_new_student_to_a_course(student_id, course_code):
    with open("students.txt") as student_file:
        student_found = False
        all_lines = student_file.readlines()
        for line in all_lines:
            line_data = line.split(";")
            if line_data[0] == student_id:
                student_found = True
                break
        if not student_found:
            print("There is no student with this id, please check the id number:")
            return

    with open("courses.txt") as course_file:
        course_found = False
        all_lines = course_file.readlines()
        for line in all_lines:
            line_data = line.split(";")
            if line_data[0] == course_code:
                course_found = True
                break
        if not course_found:
            print("There is not a course with this code, please check the code!!!")
            return

    with open("students.txt") as student_file:
        all_lines = student_file.readlines()
        student_line = ""
        for line in all_lines:
            line_data = line.split(";")
            if line_data[0] != student_id:
                continue
            else:
                student_line = line

        course_codes = student_line.split(";")[2].split(",")
        if course_code in course_codes:
            print("Student already taking this course")
            return

    with open("students.txt") as read_file:
        all_lines = read_file.readlines()
        updated_lines = []
        for line in all_lines:
            line_data = line.split(";")
            if line_data[0] != student_id:
                updated_lines.append(line)
            else:
                updated_line = line.replace("\n", "," + course_code)
                updated_line = updated_line + "\n"
                updated_lines.append(updated_line)

    with open("students.txt", "w") as write_file:
        for line in updated_lines:
            write_file.write(line)

    with open("courses.txt") as read_file:
        updated_lines = []
        for line in read_file:
            course_data = line.split(";")
            if course_data[0] != course_code:
                updated_lines.append(line)
            else:
                num_of_students = int(course_data[-1])
                num_of_students += 1
                updated_line = f"{course_code};{course_data[1]};{course_data[2]};{num_of_students}\n"
                updated_lines.append(updated_line)

    with open("courses.txt", "w") as write_file:
        for line in updated_lines:
            write_file.write(line)

    with open("courses.txt", "w") as write_file:
        for line in updated_lines:
            write_file.write(line)


def most_crowded_3_course():
    with open("courses.txt") as read_file:
        all_lines = read_file.readlines()
        courses = []
        for line in all_lines:
            course_data = line.split(";")
            courses.append([course_data[0], int(line[-2])]) #This creates ---->>['MATH1234',8(student number)],['ARTI1234',5]...]
        for i in range(len(courses)):
            for j in range(len(courses)):
                if courses[i][1] > courses[j][1]:
                    courses[i], courses[j] = courses[j], courses[i]  #This nested loop sorts our values from higher to lower.
        print(courses[0])
        print(courses[1])
        print(courses[2])


def list_most_registered_3_student():
    with open("students.txt") as read_file:
        all_lines = read_file.readlines()
        students = []
        for line in all_lines:
            student_data = line.split(";")
            students.append([student_data[0], (len(student_data[2])) / 9])    #This creates ---->>[[210709,8(course number)],[CENG1596,5]...]
        for i in range(len(students)):
            for j in range(len(students)):
                if students[i][1] > students[j][1]:
                    students[i], students[j] = students[j], students[i]    #This nested loop sorts our values from higher to lower.
        print(students[0])
        print(students[1])
        print(students[2])


def main():
    while True:
        print("Menu:")
        print("1. Add a new course")
        print("2. Search for a course by code")
        print("3. List all courses")
        print("4. List registered courses")
        print("5. Search for a course by name")
        print("6. List students and their courses")
        print("7. Register a new student to a course")
        print("8. List the 3 most crowded courses")
        print("9. List the 3 most registered students")
        print("10. Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_new_course()
            print("The new course has been added.")
        elif choice == 2:
            search_by_code()
        elif choice == 3:
            print("ALL COURSES:")
            list_all_courses()
        elif choice == 4:
            print("Courses that have at least 1 students:")
            list_registered_courses()
        elif choice == 5:
            search_by_name()
        elif choice == 6:
            print("Students and their courses:")
            students_with_their_courses()
        elif choice == 7:
            students_id = input("Please,enter an id:")
            course_code = input("Please enter a course code:")
            register_a_new_student_to_a_course(students_id, course_code)
            print("Course has been added")
        elif choice == 8:
            print("Most Crowded 3 Courses:")
            most_crowded_3_course()
        elif choice == 9:
            print("The Students Who Have Most Courses. Top 3:")
            list_most_registered_3_student()
        elif choice == 10:
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
