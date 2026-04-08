def search_notes():
    keyword = input("Enter keyword to search: ")

    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            found = False

            print("\n🔎 Search Results:")

            for note in notes:
                if keyword.lower() in note.lower():
                    print("- " + note.strip())
                    found = True

            if not found:
                print("No matching notes found.")

    except FileNotFoundError:
        print("No notes found yet.")