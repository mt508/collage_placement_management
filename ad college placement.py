import tkinter as tk
from tkinter import simpledialog, messagebox

class StudentAndCompanies:
    def __init__(self, master):
        self.master = master
        master.title("Student and Company Information")
        

        self.label_name = tk.Label(master, text="Enter your name:")
        self.label_name.grid(row=0, column=0)
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1)

        self.label_enroll = tk.Label(master, text="Enter enrollment number:")
        self.label_enroll.grid(row=1, column=0)
        self.entry_enroll = tk.Entry(master)
        self.entry_enroll.grid(row=1, column=1)

        self.label_cgpa = tk.Label(master, text="Enter CGPA:")
        self.label_cgpa.grid(row=2, column=0)
        self.entry_cgpa = tk.Entry(master)
        self.entry_cgpa.grid(row=2, column=1)

        self.label_email = tk.Label(master, text="Enter email id:")
        self.label_email.grid(row=3, column=0)
        self.entry_email = tk.Entry(master)
        self.entry_email.grid(row=3, column=1)

        self.label_phone = tk.Label(master, text="Enter your phone number:")
        self.label_phone.grid(row=4, column=0)
        self.entry_phone = tk.Entry(master)
        self.entry_phone.grid(row=4, column=1)

        self.label_course = tk.Label(master, text="Enter your course name:")
        self.label_course.grid(row=5, column=0)
        self.entry_course = tk.Entry(master)
        self.entry_course.grid(row=5, column=1)

        self.label_college = tk.Label(master, text="Enter your college name:")
        self.label_college.grid(row=6, column=0)
        self.entry_college = tk.Entry(master)
        self.entry_college.grid(row=6, column=1)

        self.label_skills = tk.Label(master, text="Skills:")
        self.label_skills.grid(row=7, column=0)
        

        self.skills = ["Python", "Java", "C++"]  # Pre-initialized skills list

        self.skills_checkboxes = []

        for i, skill in enumerate(self.skills):
            var = tk.IntVar()
            checkbox = tk.Checkbutton(master, text=skill, variable=var)
            checkbox.grid(row=7+i, column=1, sticky=tk.W)
            self.skills_checkboxes.append((skill, var))
            
            
        self.label_other=tk.Label(master,text="other skills if have")
        self.label_other.grid(row=10,column=0)
        self.entry_otherskill=tk.Entry(master)
        self.entry_otherskill.grid(row=10,column=1)
        

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_info)
        self.submit_button.grid(row=11+len(self.skills), column=0, columnspan=2)

        self.report_text = tk.Text(master, height=20, width=50)
        self.report_text.grid(row=12+len(self.skills), column=0, columnspan=2)

    def submit_info(self):
        try:
            stu_name = self.entry_name.get()
            stu_enrollno = self.entry_enroll.get()
            stu_cgpa = float(self.entry_cgpa.get())
            stu_email = self.entry_email.get().lower()  # Convert to lowercase
            stu_phone_no = self.entry_phone.get()
            stu_otherskills=self.entry_otherskill.get()

            # Phone number validation
            if not stu_phone_no.isdigit() or len(stu_phone_no) != 10:
                messagebox.showerror("Error", "Please enter a valid phone number (10 digits).")
                return

            # Email validation
            if "@" not in stu_email or "." not in stu_email:
                messagebox.showerror("Error", "Please enter a valid email address.")
                return

            stu_course = self.entry_course.get()
            stu_college = self.entry_college.get()

            selected_skills = [skill for skill, var in self.skills_checkboxes if var.get()]

            # Student information
            report = f"Student Information:\nName: {stu_name}\nEnrollment Number: {stu_enrollno}\nCGPA: {stu_cgpa}\nEmail: {stu_email}\nPhone Number: {stu_phone_no}\nCourse: {stu_course}\nCollege: {stu_college}\nSelected Skills: {', '.join(selected_skills)}\notherskilss: {stu_otherskills}\n\n"

            # Eligibility verification
            stu_cgpa = float(self.entry_cgpa.get())
            companies = ["Google", "Mahindra", "Infosys"]
            companies_eligibility = {"Google": 8.5, "Mahindra": 8.3, "Infosys": 8.2}
            eligible_companies = [company for company in companies if stu_cgpa >= companies_eligibility[company]]

            report += "Eligible Companies:\n" + ", ".join(eligible_companies) if eligible_companies else "You are not eligible for any companies."
            report += "\n\n"

            # Skills requirement check
            selected_skills = [skill for skill, var in self.skills_checkboxes if var.get()]
            companies_skills = {"Google": {"Python", "Java", "C++"}, "Mahindra": {"Python", "Java"}, "Infosys": {"Java"}}

            for company, required_skills in companies_skills.items():
                missing_skills = required_skills - set(selected_skills)
                if not missing_skills:
                    report += f"Your skills match the requirements for {company}\n"
                else:
                    report += f"Remaining skills for {company}: {', '.join(missing_skills)}\n"

            self.report_text.delete(1.0, tk.END)
            self.report_text.insert(tk.END, report)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid information.")

def main():
    root = tk.Tk()
    app = StudentAndCompanies(root)
    root.minsize(width=400, height=300)
    root.maxsize(width=400, height=800)
    root.mainloop()

if __name__ == "__main__":
    main()
