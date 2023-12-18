import json
import os
import datetime

notes_file = "notes.json"

def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, 'r') as file:
            notes = json.load(file)
        return notes
    else:
        return []

def save_notes(notes):
    with open(notes_file, 'w') as file:
        json.dump(notes, file, indent=4)

def add_note():
    notes = load_notes()
    note_id = len(notes) + 1
    title = input("Введите название заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Примечание успешно добавлено.")

def read_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}, Title: {note['title']}, Timestamp: {note['timestamp']}")
        print(f"Body: {note['body']}\n")

def edit_note():
    notes = load_notes()
    note_id = int(input("Введите идентификатор заметки, которую вы хотите отредактировать: "))
    for note in notes:
        if note['id'] == note_id:
            new_title = input("Введите новый заголовок (нажмите Enter, чтобы оставить прежний): ")
            new_body = input("Введите новое тело (нажмите Enter, чтобы оставить прежнее): ")
            if new_title:
                note['title'] = new_title
            if new_body:
                note['body'] = new_body
            note['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно изменена.")
            return
    print(f"Note with ID {note_id} not found.")

def delete_note():
    notes = load_notes()
    note_id = int(input("Введите идентификатор заметки, которую хотите удалить: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print(f"Note with ID {note_id} not found.")

def main():
    while True:
        print("\n1. Добавить заметку\n2. Прочитать заметку\n3. Изменить заметку\n4. Удалить заметку\n5. Выход")
        choice = input("Введите свой выбор: ")
        if choice == '1':
            add_note()
        elif choice == '2':
            read_notes()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")

if __name__ == "__main__":
    main()
