"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    firstLine = texts[0]
 
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    lastLine = calls[len(calls)-1]

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

print("First record of texts, " + firstLine[0] + " texts " + firstLine[1] + " at time " + firstLine[2])
print("Last record of calls, " + lastLine[0] + " calls " + lastLine[1] + " at time " + lastLine[2] +", lasting " + lastLine[3] + " seconds")

