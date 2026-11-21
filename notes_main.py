from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout

import json
app = QApplication([])

notes = {
    "Welcome!" : {
        "text" : "This is the best note taking app in the world!",
        "tags" : ["good", "instructions"]
    }
}

with open("notes_data.json", "w") as file:
    json.dump(notes, file)

notes_win = QWidget()
notes_win.setWindowTitle('The best note in thw world')
notes_win.resize(900,600)

list_notes = QListWidget()
list_notes_label = QLabel("Your Notes")

button_note_create = QPushButton('Create a note')
button_note_delete = QPushButton('Delete a note')
button_note_save = QPushButton('Save a note')

field_tag = QLineEdit('')
field_tag. setPlaceholderText('Enter a tag ... ')
field_text = QTextEdit()

button_tag_add = QPushButton('Add tag to note')
button_tag_remove = QPushButton('Untag from the note')
button_tag_search = QPushButton('Search notes by tag')

list_tags = QListWidget()
list_tags_label = QLabel('List of tags')

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget (button_note_create)
row_1.addWidget (button_note_delete)
row_2 = QHBoxLayout()
row_2.addWidget (button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

row_3 = QHBoxLayout()
row_3. addWidget (button_tag_add)
row_3.addWidget (button_tag_remove)
row_4 = QHBoxLayout()
row_4. addWidget (button_tag_search)
col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch=2)
layout_notes. addLayout(col_2, stretch=1)
notes_win.setLayout (layout_notes)

def add_note():
    note_name,ok = QInputDialog.getText(notes_win, "Add Note", "Note Name: ")
    if ok and note_name != "":
        notes[note_name] = {"text" : "", "tags" : []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]["tags"])
        print(notes)

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text. setText(notes[key]["text"])
    list_tags.clear()
    list_tags.addItems (notes [key]["tags"])

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["text"] = field_text.toPlainText()
        with open("notes_data.json", "w") as file:
            json.dump(notes,file,sort_keys=True,ensure_ascii=False)
        print(notes)
    else:
        print("Notes to save is not selected!")

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItem(notes)
        with open("notes_data.json", "w") as file:
            json.dump(notes,file,sort_keys=True,ensure_ascii=False)
        print(notes)
    else:
        print("Notes to delete is not selected!")

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tagg in notes[key]["tags"]:
            notes[key]["tags"].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open("notes_data.json", "w") as file:
            json.dump(notes,file,sort_keys=True,ensure_ascii=False)
        print(notes)
    else:
        print("Note to add a tag is not selected!")

def del_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]["tags"].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]["tags"])
        with open("notes_data.json", "w") as file:
            json.dump(notes,file,sort_keys=True,ensure_ascii=False)
        print(notes)
    else:
        print("Note to delete a tag is not selected!")

def search_tag():
    print(button_tag_search.text())
    tag = field_tag.text()
    if button_tag_search.text() == "Searching notes by tag" and tag:
        print(tag)
        notes_filtered = {}
        for notes in notes:
            if tag in notes[notes]["tags"]:
                notes_filtered[note] = notesd[note]
        button_tag_search.setText("Reset Search")
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
        print(button_tag_search.text())
    elif button_tag_search.text() == "Reset Search":
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        button_tag_search.setText("Search Notes by tag")
        print(button_tag_search.text())
    else:
        pass

list_notes.clicked.connect(add_note)
list_notes.itemClicked.connect(show_note)
list_notes.clicked.connect(save_note)
list_notes.clicked.connect(del_note)
list_notes.clicked.connect(add_tag)
list_notes.clicked.connect(del_tag)
list_notes.clicked.connect(search_tag)

notes_win. show()

with open("notes_data.json", "r") as file:
    notes = json. load(file)
list_notes.addItems (notes)

notes_win. show()
app.exec_()