# TODOLIST

todos = [
  {"id": 1, "nombre": "Estudiar", "completed": False},
  {"id": 2, "nombre": "practicar", "completed": False},
  {"id": 3, "nombre": "Limpiar", "completed": False},
]

# CRUD

# 1- Read

def show_tasks():
    pass

def create_task():
    pass

def update_task():
    pass

def delete_task():
    pass

# Menu and navigation
def menu():
    print("="*30)
    print("BIENVENIDAS AL TODO LIST")
    print("="*30)
    print(" Choose one option: create | show | delete | update | exit")
    option = input("your option: ")

    # case "create":
    #     create_task()
    # case "update":
    #     update_task()


def main():
    menu()


menu()