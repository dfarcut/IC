import csv

def export_data_to_csv(file_name,list_of_touples):
    with open(file_name,'w') as csv_file:
        field_names=['Name','Highschool','Grade']
        writer = csv.DictWriter(csv_file,fieldnames=field_names)

        writer.writeheader()
        for touple in list_of_touples:
            writer.writerow({'Name':touple[0],'Highschool':touple[1],'Grade':touple[2]})

def get_school_list_from_file(file_name):
    school_list=[]
    with open(file_name,'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            school = row['Highschool']
            if school not in school_list:
                school_list.append(school)
    return school_list

def get_data_from_file(file_name):
    data_list = []
    with open(file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            name = row['Name']
            school = row['Highschool']
            grade = row['Grade']
            data_list.append((name,school,grade))
    return data_list

