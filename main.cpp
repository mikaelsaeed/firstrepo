#include <iostream>
#include <vector>
using namespace std;

class Student {
private:
    string name;
    int age;
    float gpa;

public:
    Student(string n, int a, float g) {
        name = n;
        age = a;
        gpa = g;
    }

    void display() {
        cout << "Name: " << name 
             << ", Age: " << age 
             << ", GPA: " << gpa << endl;
    }

    string getName() {
        return name;
    }
};

class StudentManager {
private:
    vector<Student> students;

public:
    void addStudent(string name, int age, float gpa) {
        students.push_back(Student(name, age, gpa));
    }

    void showStudents() {
        for (auto &s : students) {
            s.display();
        }
    }

    void searchStudent(string name) {
        bool found = false;
        for (auto &s : students) {
            if (s.getName() == name) {
                s.display();
                found = true;
            }
        }
        if (!found) {
            cout << "Student not found\n";
        }
    }
};

int main() {
    StudentManager manager;
    int choice;

    while (true) {
        cout << "\n1. Add Student\n2. Show Students\n3. Search Student\n4. Exit\n";
        cin >> choice;

        if (choice == 1) {
            string name;
            int age;
            float gpa;

            cout << "Enter name: ";
            cin >> name;
            cout << "Enter age: ";
            cin >> age;
            cout << "Enter GPA: ";
            cin >> gpa;

            manager.addStudent(name, age, gpa);
        }
        else if (choice == 2) {
            manager.showStudents();
        }
        else if (choice == 3) {
            string name;
            cout << "Enter name to search: ";
            cin >> name;
            manager.searchStudent(name);
        }
        else if (choice == 4) {
            break;
        }
        else {
            cout << "Invalid choice\n";
        }
    }

    return 0;
}