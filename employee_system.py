import tkinter as tk
from tkinter import messagebox

# Lista para armazenar os funcionários
employee_list = []
global_id = 1  # ID único para cada funcionário


# Função para cadastrar um novo funcionário
def register_employee():
    global global_id

    name = entry_name.get()
    department = entry_department.get()
    salary = entry_salary.get()

    if not name or not department or not salary:
        messagebox.showwarning("Input Error", "Please fill out all fields.")
        return

    employee = {
        "id": global_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employee_list.append(employee)
    global_id += 1

    messagebox.showinfo("Success", f"Employee {name} registered!")
    clear_entries()
    update_display()


# Função para remover funcionário por ID
def remove_employee():
    remove_id = entry_remove_id.get()
    for e in employee_list:
        if str(e["id"]) == remove_id:
            employee_list.remove(e)
            messagebox.showinfo("Success", f"Employee ID {remove_id} removed.")
            update_display()
            return
    messagebox.showerror("Error", "Employee ID not found.")


# Atualiza a área de exibição com todos os funcionários
def update_display():
    display_text.delete("1.0", tk.END)
    for e in employee_list:
        display_text.insert(tk.END, f"ID: {e['id']} | Name: {e['name']} | Dept: {e['department']} | Salary: {e['salary']}\n")


# Limpa os campos de entrada
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_department.delete(0, tk.END)
    entry_salary.delete(0, tk.END)


# Criação da janela principal
window = tk.Tk()
window.title("Employee Management System")
window.geometry("500x600")

# Título
tk.Label(window, text="Register New Employee", font=("Helvetica", 14, "bold")).pack(pady=10)

# Entradas de dados
tk.Label(window, text="Name").pack()
entry_name = tk.Entry(window, width=40)
entry_name.pack()

tk.Label(window, text="Department").pack()
entry_department = tk.Entry(window, width=40)
entry_department.pack()

tk.Label(window, text="Salary").pack()
entry_salary = tk.Entry(window, width=40)
entry_salary.pack()

# Botão de cadastro
tk.Button(window, text="Register Employee", command=register_employee).pack(pady=10)

# Exibição de funcionários
tk.Label(window, text="Registered Employees", font=("Helvetica", 12, "bold")).pack()
display_text = tk.Text(window, height=10, width=60)
display_text.pack()

# Área de remoção
tk.Label(window, text="Remove Employee by ID", font=("Helvetica", 12, "bold")).pack(pady=10)
entry_remove_id = tk.Entry(window, width=20)
entry_remove_id.pack()
tk.Button(window, text="Remove Employee", command=remove_employee).pack(pady=5)

# Inicia a interface
window.mainloop()
