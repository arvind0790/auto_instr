import csv
class datalog(object):

    def __init__(self,filename):
        self.filename = filename

    def data(var1):
        with open(datalog.filename + '.csv', 'a', newline='') as csvfile:
            mywriter1 = csv.writer(csvfile, delimiter=',', dialect='excel')
            mywriter1.writerow(var1)

    def header(var1, *var):
        with open(datalog.filename+ '.csv', 'a', newline='') as csvfile:
            mywriter2 = csv.DictWriter(csvfile, dialect='excel', fieldnames=[var1, *var])
            mywriter2.writeheader()