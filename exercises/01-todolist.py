# TODOLIST
todos = [
  {"id": 1, "nombre": "Estudiar", "completed": False},
  {"id": 2, "nombre": "practicar", "completed": False},
  {"id": 3, "nombre": "Limpiar", "completed": True},
]

# CRUD
def show_tasks():
    print("-"*37)
    print("Tareas")
    print("-"*37)

    for index,todo in enumerate(todos):
        todo_completed = "|X|" if todo["completed"] else "| |"
        print(f"{index + 1} - {todo["nombre"]} {todo_completed}")
    print("-"*37)

def create_task():
    pass

def update_task():
    pass

def delete_task():
    pass

def exit():
    print("-"*37)
    print("Gracias por usar la aplicación")
    print("-"*37)


# Menu and navigation
def menu():
    print("-"*37)
    print("bienvenida a tu organizador de tareas")
    print("-"*37)

    while True:
        print("| CREATE | DELETE | UPDATE | SHOW | EXIT")
        option = input("Choose one option: ").upper()
        match option:
            case "CREATE":
                # return create_task(todos)
                pass
            case "SHOW":
                show_tasks()
            case "DELETE":
                pass
                # return delete_task()
            case "UPDATE":
                pass
                # return update_task()
            case "EXIT":
                return exit()


def main():
    menu()


main()

