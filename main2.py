# Imports required
from tkinter import *
from tkinter import filedialog
import json
import csv

class convertor_2_json:
    file_path = ''

    def upload_file(self):
        """This function is to upload the CSV file into the Program"""

        self.file_path = filedialog.askopenfilename(initialdir="C:/Users",
                                              title="Select a file", filetypes=(("csv files", "*.csv"),
                                                                                ("all files", "*.*")))
        self.read_file(self.file_path)


    def read_file(self, file_path):
        """This Function reads the Uploaded CSV and convert in into the required format"""
        # open the csv
        try:
            with open(file_path, 'r') as f:
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
            self.dump_file(data)
        except FileNotFoundError:
            print("File was not found!")

    def dump_file(self, data):
        """This functions dumps the data into JSON format and make a txt file containing the Json Data.  """

        with open('struct.json', 'w') as f:
            json.dump(data, f, indent=4)

        head_label3 = Label(root,
                            text='Your data has been converted into Json in the notepad file. Please close the program.').pack()


if __name__ == '__main__':
    file_path_main = ''
    root = Tk()
    root.title('CSV to Json Converter')
    root.geometry('644x344')
    head_label = Label(root, text='Welcome to CSV to Json convertor').pack()
    head_label2 = Label(root, text='Please upload the CSV to convert').pack()

    convertor_obj = convertor_2_json()

    try:
        my_btn = Button(root, text="Upload File", command=convertor_obj.upload_file).pack()
    except EXCEPTION as e:
        print(e)

    root.mainloop()


