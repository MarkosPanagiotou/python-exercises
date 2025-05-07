import os

FILENAME = "tasks.txt"


def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")


def show_menu():
    print("\nΕπιλογές:")
    print("1. Προσθήκη εργασίας")
    print("2. Διαγραφή εργασίας")
    print("3. Εμφάνιση όλων των εργασιών")
    print("4. Έξοδος")


def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("Δώσε επιλογή (1-4): ").strip()

        if choice == "1":
            new_task = input("Γράψε την εργασία που θέλεις να προσθέσεις: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print("Η εργασία προστέθηκε επιτυχώς.")
            else:
                print("Η εργασία δεν μπορεί να είναι κενή.")

        elif choice == "2":
            if not tasks:
                print("Δεν υπάρχουν εργασίες για διαγραφή.")
                continue
            print("\nΕργασίες:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
            try:
                del_index = int(input("Δώσε τον αριθμό της εργασίας για διαγραφή: "))
                if 1 <= del_index <= len(tasks):
                    deleted = tasks.pop(del_index - 1)
                    save_tasks(tasks)
                    print(f"Η εργασία \"{deleted}\" διαγράφηκε.")
                else:
                    print("Μη έγκυρος αριθμός.")
            except ValueError:
                print("Παρακαλώ δώσε έναν έγκυρο αριθμό.")

        elif choice == "3":
            if not tasks:
                print("Δεν υπάρχουν εργασίες.")
            else:
                print("\nΛίστα εργασιών:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")

        elif choice == "4":
            print("Έξοδος από το πρόγραμμα.")
            break

        else:
            print("Μη έγκυρη επιλογή. Δοκίμασε ξανά.")

if __name__ == "__main__":
    main()