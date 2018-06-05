import csv
import os

csv_file_folder = "your_all_csv_path/csv/"

def write_headers_csv_for_input_file(master_csv_path):
    csvfile = open( master_csv_path, 'aw')
    fileEmpty = os.stat(master_csv_path).st_size == 0
    fieldnames = ['class','label', 'url', 'xmin','ymin','xmax','ymax','extra']
    with csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if fileEmpty:
            writer.writeheader()
for filename in os.listdir(csv_file_folder):
    if (filename.endswith('.csv')):
        full_path  = csv_file_folder + filename
        master_csv_path = csv_file_folder + "MASTER.csv"
        write_headers_csv_for_input_file(master_csv_path)

        output_dictionary = {}
        read_data = csv.DictReader(open(full_path))
        for data_in in read_data:
            output_dictionary["class"] = data_in['class']
            output_dictionary["label"] = data_in['label']
            output_dictionary["url"] = data_in['url']
            output_dictionary["xmin"] = data_in['xmin']
            output_dictionary["ymin"] = data_in['ymin']
            output_dictionary["xmax"] = data_in['xmax']
            output_dictionary["ymax"] = data_in['ymax']
            output_dictionary["extra"] = data_in['extra']

            csvfile_write = open(master_csv_path , 'aw')
            fileEmpty = os.stat(master_csv_path).st_size == 0
            fieldnames = ['class','label', 'url', 'xmin','ymin','xmax','ymax','extra']
            with csvfile_write:
                writer = csv.DictWriter(csvfile_write, fieldnames=fieldnames)
                if fileEmpty:
                    writer.writeheader()
                writer.writerow(output_dictionary)
