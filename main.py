from tkinter import *
from tkinter import filedialog
import json
import csv

root = Tk()
root.title('CSV to Json Converter')
root.geometry('644x344')
head_label = Label(root, text='Welcome to CSV to Json convertor').pack()
head_label2 = Label(root, text='Please upload the CSV to convert').pack()
fname = ''
def upload():
    global fname
    filename = filedialog.askopenfilename(initialdir="C:/Users",
                                          title="Select a file", filetypes=(("csv files", "*.csv"),
                                                                            ("all files", "*.*")))
    print(filename)
    fname = filename
    read_file(filename)


def read_file(filename):
    # opent the csv
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        # skipping the first line
        next(reader)
        data = {'label': '', 'id': '', 'link': '', 'children': []}
        # main logic for iterating the csv
        for row in reader:
            data['label'] = row[1]
            data['id'] = row[2]
            data['link'] = row[0]
            data['children'].append({'label': row[4], 'id': row[5], 'link': row[6],
                                     'children': [{'label': row[7], 'id': row[8], 'link': row[9], 'children': []}]})
            print(data)
    print(data)
    dump_file(data)

def dump_file(data):
    # dumping the data into the json
    with open('struct.json', 'w') as f:
        json.dump(data, f, indent=2)

    head_label3 = Label(root,
                        text='Your data has been converted into Json in the notepad file. Please close the program.').pack()


my_btn = Button(root, text="Upload File", command=upload).pack()

root.mainloop()
