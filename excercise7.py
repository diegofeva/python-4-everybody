# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values
# and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

count=0
value=0

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: Yo can just hit enter if you desiree")
if len(fname) < 1:
    fname = "excercises\data\mbox-short.txt"
fh = open(fname)

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    
    intervalil = line.find(":")
    
    
    
    interval = line[intervalil+1:]
    
    
    intervalstrip = interval.strip()
    intervalfloat = float(intervalstrip)
    value = value + intervalfloat
    answer = value/count
    
print("Average spam confidence:",answer)
