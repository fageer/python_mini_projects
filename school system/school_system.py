import sqlite3


conn = sqlite3.connect("school system/students.db")
cursor = conn.cursor()


class Student:
    students = []
    std_co = 0


    def __init__(self, name, phonenumber, course=""):
        self.name = name
        self.phonenumber = phonenumber
        self.course = course


    def add_students(self):
        std_count = int(input("How many students do you want to add? "))
        cursor.execute("""CREATE TABLE IF NOT EXISTS students
                  (
                      std_name TEXT, 
                      std_phone TEXT, 
                      std_course TEXT
                  )
               """)
        while std_count > 0:
            name = input("Student name: ").strip()
            phonenumber = input("Student phonenumber: ").strip()
            course = input("Student course: ").strip()
            cursor.execute("INSERT INTO students VALUES (?, ?, ?)", (name, phonenumber, course))
            std_count -= 1
            Student.std_co += 1

        conn.commit()  
        print("Students Added Successfully ✅.")


    def show_all_students(self):
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        if not result:
            print("Sorry You Don't Have Any Student.")
        for key, row in enumerate(result):
            print(f"Student{key+1} Name: {row[0]}, Phone: {row[1]}, Course: {row[2]}.")
    

    def show_student_count(self):
        cursor.execute("SELECT COUNT(*) FROM students")
        result = cursor.fetchone()[0]
        if result > 0:
            print(f"You Have {result} Students.")
        else:
            print(f"Sorry You Don't Have Any Student.")
    
    
    def show_specific_student(self, std_name):
        cursor.execute("SELECT * FROM students WHERE std_name = ?", (std_name,))
        result = cursor.fetchone()
        if result:
            print(f"'{std_name}' Found ✅.")
            print(print(f"Student Name: {result[0]}, Phone: {result[1]}, Course: {result[2]}."))
        else:
            print(f"Sorry '{std_name}' Not Found ❌.") 


    def remove_student(self, studentname):
        cursor.execute("DELETE FROM students WHERE std_name = ?", (studentname,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"'{studentname}' Has Been Deleted Successfully ✅.")
        else:
            print(f"Sorry '{studentname}' Not Found ❌.")   


def main():
    print("=" * 10, "🏫 Welcome to Fager School 🏫", "=" * 10)
    admin = input("Are you an admin in this school? ").lower()
    if admin in ['y', 'yes']:
        print("That's great! 👏.")
        name = input("Enter Username: ").lower()
        password = input("Enter Password: ")
        if name != 'fager' or password != '12345':
            raise ValueError("Sorry, Invalid Username or Password ❌.")
        s1 = Student(name, password)
        print("Login Successfully ✅.")
       
        while True:
            menu = f"""
Hello Mr.{name}🙏. What Would You Like To Do:
1- Add a student.
2- Show all students.
3- Show the number of students.
4- Show a specific student.
5- Delete a student.
6- Exit.
            """

            print("=" * 10, "🏫 Welcome to Fager School 🏫", "=" * 10)
            print(menu)

            try:
            
                choice = int(input("Enter the number of your choice: "))

                if choice == 1:
                    s1.add_students()
                elif choice == 2:
                    s1.show_all_students()
                elif choice == 3:
                    s1.show_student_count()
                elif choice == 4:
                    student_name = input("Enter the student name you want to search: ").strip()
                    s1.show_specific_student(student_name)
                elif choice == 5:
                    student_name = input("Enter the student name you want to delete: ").strip()
                    s1.remove_student(student_name)
                elif choice == 6:
                    exit()
                else:
                    print("Invalid choice! . Please enter a number between 1 and 5.")

            except ValueError:
                print("Invalid input !. Please enter a valid number.")

            done = input("Do you want to go to the home page? ").lower().strip()

            while done not in ["y", "yes", "n", "no"]:
                done = input("Invalid input. Enter 'Y' or 'YES' to continue or 'N' or 'NO' to exit: ").lower().strip()

            if done in ["n", "no"]:
                break
    else:
        print("Sorry, You are Not Admin ❌.")

    print("Thanks for choosing Fager School. We appreciate your choice! 🙏.")





if __name__ == "__main__":
    main()
