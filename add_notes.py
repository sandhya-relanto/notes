def add_note():
    note = input("Enter your note: ")
 
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
 
    print("✅ Note added successfully!")