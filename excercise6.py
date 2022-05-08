# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# .Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

y=len(text)

x=text.find("0")


answer = text[x:y+1]
print(float(answer))