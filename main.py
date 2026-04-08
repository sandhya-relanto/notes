from add_notes import add_note

from view_notes import view_notes

from search_notes import search_notes
 
 
def menu():

    while True:

        print("\n==== Team Notes App ====")

        print("1. Add Note")

        print("2. View Notes")

        print("3. Search Notes")

        print("4. Exit")
 
        choice = input("Enter your choice: ")
 
        if choice == "1":

            add_note()

        elif choice == "2":

            view_notes()

        elif choice == "3":

            search_notes()

        elif choice == "4":

            print("👋 Exiting...")

            break

        else:

            print("Invalid choice. Try again.")
 
 
if __name__ == "__main__":

    menu()
 