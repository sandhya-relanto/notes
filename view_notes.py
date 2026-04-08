def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
 
            if not notes:
                print("No notes found.")
            else:
                print("\n📌 Your Notes:")
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note.strip()}")
 
    except FileNotFoundError:
        print("No notes file found. Add notes first.")