"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
 
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

txtPhoneNums = [item[0] for item in texts] + [item[1] for item in texts]
txtPhoneNumsSet = set(txtPhoneNums);

callPhoneNums = [item[0] for item in calls] + [item[1] for item in calls]
callPhoneNumsSet = set(callPhoneNums);

uniqPhoneNums = txtPhoneNumsSet.union(callPhoneNumsSet)

totalPhoneNums = len(uniqPhoneNums)

print("There are " + str(totalPhoneNums) + " different telephone numbers in the records.")
