# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file")
if len(name) < 1:
    name = "excercises/data/mbox-short.txt"

list_emails = list()
emails_dict = dict()
handle = open(name)
i=0

for line in handle:
    line_strip = line.rstrip()
    if not line_strip.startswith("From "):
        continue
    line_split = line_strip.split()
    list_emails.append(line_split[1])


for email in list_emails:
    if email not in emails_dict:
        emails_dict[email] = 1
    else:
        emails_dict[email] = emails_dict[email] + 1

max_count = max(emails_dict.values())
for email,count in emails_dict.items():
    if count == max_count:
        print(email,emails_dict[email])

