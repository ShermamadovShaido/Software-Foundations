def calculate_average(scores):
  return sum(scores) /len(scores)

def assign_grade(average):
  if average >= 85:
    return 'A'
  elif average >= 75:
    return 'B'
  elif average >= 65:
    return 'C'
  elif average >= 50:
    return 'D'
  else:
    return 'F'
  import csv
from utils import calculate_average, assign_grade
 
def process_grades():
    students = []
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name, math, science, english=row
            average = calculate_average([int(math), int(science),int(english)])
            grade = assign_grade(average)
            students.append([name, int(average), grade])
 
    with open('student_results2.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Average', 'Grade'])
        writer.writerows(students)
    print('Results saved to student_results2.csv')
    from process_data import process_grades
if __name__ == '__main__':
    process_grades()
 