import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        label_status.config(text="", fg="black")
    else:
        label_status.config(text="Please enter a task!", fg="red")

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
        label_status.config(text="", fg="black")
    except IndexError:
        label_status.config(text="No task selected!", fg="red")

def update_task():
    try:
        index = listbox_tasks.curselection()[0]
        task = entry_task.get()
        if task:
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, task)
            entry_task.delete(0, tk.END)
            label_status.config(text="", fg="black")
        else:
            label_status.config(text="Please enter a task to update!", fg="red")
    except IndexError:
        label_status.config(text="No task selected!", fg="red")

root = tk.Tk()
root.title("To-do List")

# Creating a large labeled frame with orange background for tasks
frame_tasks = tk.LabelFrame(root, text="Tasks", bg="orange", fg="black", padx=10, pady=10, font=("Helvetica", 12))
frame_tasks.pack(pady=10, padx=10, fill="both", expand=True)

listbox_tasks = tk.Listbox(frame_tasks, height=20, width=60)
listbox_tasks.pack(side=tk.LEFT, padx=10, pady=10)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Creating a labeled frame for task input
frame_input = tk.LabelFrame(root, text="Task Input", fg="black", padx=10, pady=10, font=("Helvetica", 12))
frame_input.pack(pady=10, padx=10, fill="both", expand=True)

entry_task = tk.Entry(frame_input, width=58)
entry_task.pack(pady=5)

button_add_task = tk.Button(frame_input, text="Add Task", width=56, command=add_task, bg="orange", fg="black")
button_add_task.pack(pady=2)

button_delete_task = tk.Button(frame_input, text="Delete Task", width=56, command=delete_task, bg="orange", fg="black")
button_delete_task.pack(pady=2)

button_update_task = tk.Button(frame_input, text="Update Task", width=56, command=update_task, bg="orange", fg="black")
button_update_task.pack(pady=2)

label_status = tk.Label(root, text="", fg="black")
label_status.pack(pady=5)

root.mainloop()
