import csv

def searchbyage():
    age =(input('Enter the age group for COVID-19 cases you are looking for:\n ')
    csv_file =csv.reader(open('BCCase_Details.csv','r'))

    for row in csv_file:
        if age == row[4]:
            print(row)
        else:
            break

    csv_file.close()


#function is not working