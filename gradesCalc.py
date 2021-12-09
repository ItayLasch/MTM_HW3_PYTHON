#### PART 1 ####
# is_line_valid: checks if the line with the description of the student is valid
# according to the rules. returns True if it's okay, false otherwise.
#   splited_list: A list that conatins the student's ID,name,course number and his grade
#   in that course.
def is_line_valid(splited_list) -> bool:
    id = splited_list[0].strip()
    name = splited_list[1].strip()
    course_number = int(splited_list[2].strip())
    avg_grade = int(splited_list[3].strip())
    if(id[0] == '0' or len(id) != 8):
        return False
    if not all(letter.isalpha() or letter.isspace() for letter in name):
        return False
    if(course_number < 1):
        return False
    if(avg_grade <= 50 or avg_grade > 100):
        return False

    return True

# final_grade_calc: calculates the final grade of the student and returns
# it according to the rules.
#   id_digits: Last two digits of the student id.
#   avg_grade: The average grade of the student.
def final_grade_calc(id_digits: str, avg_grade: str) -> int:
    return ((int(id_digits) + int(avg_grade))//2)

# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output
def final_grade(input_path: str, output_path: str) -> int:
    if(input_path == None or input_path == ""):
        return 0
    input_file = open(input_path, 'r')
    output_file = open(output_path, 'w')
    students_grades = {}
    total_grade, counter = 0, 0
    for line in input_file:
        splited = line.split(',')
        if(is_line_valid(splited) == True):
            students_grades[splited[0].strip()] = splited[3].strip()

    for key in sorted(students_grades):
        last_digits = key.strip()[6:8]
        final_grade = final_grade_calc(last_digits, students_grades[key])
        input = key + ", " + str(int(students_grades[key])) + ", " +str(final_grade)+ "\n"
        output_file.write(input)
        total_grade += final_grade
        counter += 1
    input_file.close()
    output_file.close()

    if(counter != 0):
        return (total_grade//counter)

    return 0


#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def check_strings(s1: str, s2: str) -> bool:
    s2_letters = [letter for letter in s2.lower()]
    for letter in s1.lower():
        if (s2_letters.count(letter) == 0):
            return False
        s2_letters.remove(letter)

    return True
