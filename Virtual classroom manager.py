
#Defining a Python class called VirtualClassroomManager 
#to manage virtual classrooms, students, and assignments.

class VirtualClassroomManager:
    def __init__(self):
        self.classrooms = {}
        self.students = {}
        self.assignments = {}

#Method for adding a virtual classroom, student, schedule assignment and update submit assignment
 #to the manager with checks for existence and feedback messages
    def add_classroom(self, class_name):
        if class_name not in self.classrooms:
            self.classrooms[class_name] = []
            print(f"Classroom : '{class_name}' has been created.")
        else:
            print(f"Classroom : '{class_name}' already exists.")

    def add_student(self, student_id, class_name):
        if class_name in self.classrooms:
            if student_id not in self.students:
                self.students[student_id] = class_name
                self.classrooms[class_name].append(student_id)
                print(f"Student : '{student_id}' has been enrolled in {class_name}.")
            else:
                print(f"Student : '{student_id}' is already enrolled in a class.")
        else:
            print(f"Classroom : '{class_name}' does not exist.")

    def schedule_assignment(self, class_name, assignment_details):
        if class_name in self.classrooms:
            assignment = {"class": class_name, "details": assignment_details}
            if class_name in self.assignments:
                self.assignments[class_name].append(assignment)
            else:
                self.assignments[class_name] = [assignment]
            print(f"Assignment for '{class_name}' has been scheduled.")
        else:
            print(f"Classroom '{class_name}' does not exist.")

    def submit_assignment(self, student_id, class_name, assignment_details):
        if student_id in self.students and self.students[student_id] == class_name:
            if class_name in self.assignments:
                for assignment in self.assignments[class_name]:
                    if assignment["details"] == assignment_details:
                        print(f"Assignment submitted by Student '{student_id}' in '{class_name}'.")
                        return
                print(f"No matching assignment found for '{class_name}'.")
            else:
                print(f"No assignments scheduled for '{class_name}'.")
        else:
            print(f"Student '{student_id}' is not enrolled in '{class_name}'.")

# Initialize the VirtualClassroomManager
manager = VirtualClassroomManager()

# Main loop to take user input and execute commands
while True:
    user_input = input("Enter a command (Type 'exit' to quit): ").strip().split()
    if not user_input:
        continue

    command = user_input[0].lower()

    if command == 'add_classroom':
        if len(user_input) > 1:
            class_name = ' '.join(user_input[1:])
            manager.add_classroom(class_name)
        else:
            print("Please provide a class name.")

    elif command == 'add_student':
        if len(user_input) > 2:
            student_id = user_input[1]
            class_name = ' '.join(user_input[2:])
            manager.add_student(student_id, class_name)
        else:
            print("Please provide student ID and class name.")

    elif command == 'schedule_assignment':
        if len(user_input) > 2:
            class_name = user_input[1]
            assignment_details = ' '.join(user_input[2:])
            manager.schedule_assignment(class_name, assignment_details)
        else:
            print("Please provide class name and assignment details.")

    elif command == 'submit_assignment':
        if len(user_input) > 3:
            student_id = user_input[1]
            class_name = user_input[2]
            assignment_details = ' '.join(user_input[3:])
            manager.submit_assignment(student_id, class_name, assignment_details)
        else:
            print("Please provide student ID, class name, and assignment details.")

#Allows the user to exit the program and terminates the loop
    elif command == 'exit':
        break

#Allows the user to exit the program and terminates the loop
    else:
        print("Invalid command. Please try again.")
