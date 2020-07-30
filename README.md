# attendance_counter

A Simple Python Script to count number of days present for a specified name/roll number from csv/excel files exported from Microsoft Teams.

## Usage

Download this repository using the "Clone/Download" option
Save the attendance .csv/.xlsx files in the same folder as this repository
Run the following command in the Terminal:


If files are .csv:
```
pip3 install -r requirements.txt
python3 csv_files.py [Search Term]
```

If files are .xlsx:
```
pip3 install -r requirements.txt
python3 excel_files.py [Search Term]
```

"Search Term" must be the Name/Roll Number specified exactly as mentioned in the Attendance CSV/Excel File.
