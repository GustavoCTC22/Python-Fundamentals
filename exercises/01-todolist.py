import uuid

# TODOLIST
todos = [
  {"id": "121", "nombre": "Estudiar", "completed": False},
  {"id": "214", "nombre": "practicar", "completed": False},
  {"id": "2f5", "nombre": "Limpiar", "completed": True},
]

# CRUD
def show_tasks():
    print("-"*37)
    print("Tareas")
    print("-"*37)

    for todo in todos:
        todo_completed = "|X|" if todo["completed"] else "| |"
        print(f"{todo["id"]} - {todo["nombre"]} {todo_completed}")
    print("-"*37)

def create_task():
    while True:
        task_name = input("Write the name: ")
        if not task_name.strip() == "":
            new_task = {
                "id": str(uuid.uuid1())[:3],
                "nombre": task_name,
                "completed": False
            }
            todos.append(new_task)   
            break

def update_task():
    show_tasks()
    while True:
        task_id = input("Select todo by ID: ")
        if any(todo["id"] == task_id for todo in todos):
            new_name = input("Introduce new task name: ")
            for todo in todos:
                if todo["id"] == task_id:
                    todo["nombre"] = new_name
                    break
            print(new_name)
            break
        print("ID provided doesnt exists")


def delete_task():
    show_tasks()
    task_id = input("Select todo by ID: ")
    # todos_updated = list(filter(lambda todo: todo["id"] != task_id, todos))
    # return todos_updated
    for todo in todos:
        if todo["id"] == task_id:
            todos.remove(todo) 
            print("tarea eliminada con éxito")
            break
            

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
                create_task()
            case "SHOW":
                show_tasks()
            case "DELETE":
                # global todos
                delete_task()
            case "UPDATE":
                update_task()
            case "EXIT":
                return exit()


def main():
    menu()


main()

