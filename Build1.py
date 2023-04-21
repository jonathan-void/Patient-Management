import tkinter
from tkinter import ttk, Label
from tkinter import messagebox

#TEST FILE 2 : TEST COMPLETED

def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        fullname = firstname + lastname

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            phone = phone_entry.get()

            # Medical Info
            gender = gender_combobox.get()
            bp = bp_status_var.get()
            diabetes = diabetes_status_var.get()
            cardiac = cardiac_status_var.get()
            past_history = past_history_entry.get()
            medicines = current_medicines_enter.get()
            allergies = allergies_enter.get()
            habits = habits_enter.get()
            other = others_enter.get()
            complaint = complaint_entry.get()
            previous = lastyear_entry.get()

            file_name = "{}.txt".format(fullname)

            with open(file_name, "w") as f:
                f.write("MAIN INFORMATION:\n")
                f.write("\n")
                f.write("Name                 : {} {} {}\n".format(title, firstname, lastname))
                f.write("Phone Number         : {}\n".format(phone))
                f.write("Age                  : {}\n".format(age))
                f.write("Nationality          : {}\n".format(nationality))
                f.write("\n")
                f.write("MEDICAL INFORMATION:\n")
                f.write("\n")
                f.write("Gender               : {}\n".format(gender))
                f.write("Medical History      : {}, {}, {}\n".format(bp, diabetes, cardiac))
                f.write("Past Medical History : {}\n".format(past_history))
                f.write("\n")
                f.write("ENTRA INFORMATION:\n")
                f.write("\n")
                f.write("Current Medicines    : {}\n".format(medicines))
                f.write("Allergies            : {}\n".format(allergies))
                f.write("Habits               : {}\n".format(habits))
                f.write("Other Info           : {}\n".format(other))
                f.write("\n")
                f.write("DENTAL INFORMATION:\n")
                f.write("\n")
                f.write("Main Complaint       : {}\n".format(complaint))
                f.write("Previous Treatments  : {}\n".format(previous))
                f.write("\n")
                # f.write("----------------------------------------------------\n")

        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not consented the treatment")


window = tkinter.Tk()
window.title("Data Entry Form")

# Simply set the theme
window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "light")

frame = tkinter.Frame(window)
frame.pack()

# Saving Patient Info
user_info_frame = tkinter.LabelFrame(frame, text="Patient Information")
user_info_frame.grid(row=0, column=0, padx=50, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Mrs.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=120)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["India", "Other"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

phone_label = tkinter.Label(user_info_frame, text="Phone Number")
phone_label.grid(row=2, column=2)

phone_entry = tkinter.Entry(user_info_frame)
phone_entry.grid(row=3, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=50, pady=5)

# Medical Info
medical_frame = tkinter.LabelFrame(frame, text="Medical Information")
medical_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

gender_label: Label = tkinter.Label(medical_frame, text="Gender")
gender_status_var = tkinter.StringVar(value="Gender")
gender_combobox = ttk.Combobox(medical_frame, values=["Male", "Female"])

gender_label.grid(row=0, column=0)
gender_combobox.grid(row=1, column=0)

medical_history_label = tkinter.Label(medical_frame, text="Medical History")
medical_history_label.grid(row=0, column=2)

bp_status_var = tkinter.StringVar(value="Blood Pressure")
# bp_label = tkinter.Label(medical_frame, text="Blood Pressure")
bp_check = tkinter.Checkbutton(medical_frame, text="Blood Pressure", variable=bp_status_var, onvalue="Blood Pressure",
                               offvalue="NIL")
bp_check.grid(row=1, column=1)

diabetes_status_var = tkinter.StringVar(value="Diabetes")
# diabetes_label = tkinter.Label(medical_frame, text="Diabetes")
diabetes_check = tkinter.Checkbutton(medical_frame, text="Diabetes", variable=diabetes_status_var, onvalue="Diabetes",
                                     offvalue="NIL")
diabetes_check.grid(row=1, column=2)

cardiac_status_var = tkinter.StringVar(value="Cardiac Problems")
# cardiac_label = tkinter.Label(medical_frame, text="Cardiac Problems")
cardiac_check = tkinter.Checkbutton(medical_frame, text="Cardiac Problems", variable=cardiac_status_var,
                                    onvalue="Cardiac Problems", offvalue="NIL")
cardiac_check.grid(row=1, column=3)

past_history_label = tkinter.Label(medical_frame, text="Past Medical History")
past_history_label.grid(row=0, column=4)
past_history_entry = tkinter.Entry(medical_frame)
past_history_entry.grid(row=1, column=4)
note_label = tkinter.Label(medical_frame, text="Note: If None type NIL.")
note_label.grid(row=2, column=4)

for widget in medical_frame.winfo_children():
    widget.grid_configure(padx=20, pady=5)

# Extra Info

extra_frame = tkinter.LabelFrame(frame, text="Extra Information")
extra_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

current_medicines_label = tkinter.Label(extra_frame, text="Current Medicines")
current_medicines_label.grid(row=0, column=0)
current_medicines_enter = tkinter.Entry(extra_frame)
current_medicines_enter.grid(row=1, column=0)

allergies_label = tkinter.Label(extra_frame, text="Allergies")
allergies_label.grid(row=0, column=1)
allergies_enter = tkinter.Entry(extra_frame)
allergies_enter.grid(row=1, column=1)

habits_label = tkinter.Label(extra_frame, text="Habits")
habits_label.grid(row=0, column=2)
habits_enter = tkinter.Entry(extra_frame)
habits_enter.grid(row=1, column=2)

others_label = tkinter.Label(extra_frame, text="Other (If Any)")
others_label.grid(row=0, column=3)
others_enter = tkinter.Entry(extra_frame)
others_enter.grid(row=1, column=3)

for widget in extra_frame.winfo_children():
    widget.grid_configure(padx=30, pady=5)

# Dental Info

dental_frame = tkinter.LabelFrame(frame, text="Dental Information")
dental_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

complaint_label = tkinter.Label(dental_frame, text="What is your main complaint")
complaint_label.grid(row=0, column=0)
complaint_entry = tkinter.Entry(dental_frame, width=110)
complaint_entry.grid(row=1, column=0)

lastyear_label = tkinter.Label(dental_frame, text="Treatments done in the last year")
lastyear_label.grid(row=3, column=0)
lastyear_entry = tkinter.Entry(dental_frame, width=110)
lastyear_entry.grid(row=4, column=0)

for widget in dental_frame.winfo_children():
    widget.grid_configure(padx=10, pady=2)

# Consent
consent_frame = tkinter.LabelFrame(frame, text="Consent")
consent_frame.grid(row=4, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(consent_frame, text="I Hereby Consent The Treatment Procedure",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=5, column=0, sticky="news", padx=20, pady=10)

window.mainloop()