# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name= "mbox-short.txt"
handle = open(name)
email_hour_list = list()
hour_dict = dict()
count = 0

for lines in handle:
    lines_rstrip = lines.rstrip()
    if not lines_rstrip.startswith("From "):
        continue
    else:
        line_split = lines_rstrip.split()
        email_time = line_split[5]
        email_time_split = email_time.split(":")
        email_hour_list.append(email_time_split[0])

for hour in email_hour_list:
    if hour not in hour_dict:
        hour_dict[hour] = 1
    else:
        hour_dict[hour] = hour_dict[hour] + 1

answer=sorted(hour_dict.items())

for k,v in answer:
    print(k,v)