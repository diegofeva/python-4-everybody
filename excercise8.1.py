fname = input("Enter file name: Or you can just hit enter if you want ")
if len(fname) <1:
    fname = 'excercises/data/romeo.txt'
fh = open(fname)
lst=[]


sentence = fh.read()
words_list = sentence.split()

lenght = len(words_list)
                  


words_list.sort()


for i in range(lenght):

    if words_list.count(words_list[i]) == 1:
        lst.append(words_list[i])

    if words_list.count(words_list[i]) == 2:
        words_list[i] = "control object"

    if words_list.count(words_list[i]) == 3:
        words_list[i] = "control object"




print(lst)
        
        
        
    
     