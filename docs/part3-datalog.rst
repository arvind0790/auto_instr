==================================
datalog
==================================

This class is written for saving the measured data in a csv file. It supports following methods.

-----------------
Creating filename
-----------------
- Syntax: filename('Enter_the_filename')
- Description: This method assigns the entered filename to the csv file. This method must be called before using any other method of this class.

------
Header
------
- Syntax: header('header1','header2',...)
- Description: This method creates the header row in the csv file. It accepts at least one argument.

----------------
Logging the Data
----------------
- Syntax: data([data_list])
- Description: This method saves the measured data (list) in the csv file ,it only accepts one argument. It's advisable to save the multiple data points in a list form before entering it into this method.

---------
Examples
---------
- **datalog.filename('my_experiment')** , creates the filename.
- **datalog.header('device_number','temperature','voltage')** , opens the my_experiment.csv file and writes (appends) the row with header arguments.
- **datalog.data([1,'25C',2.3])** , appends the entered data in the csv file.

