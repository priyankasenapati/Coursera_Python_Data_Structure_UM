# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.



fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word = line.rstrip().split()
    for element in word:           # check every element in word
        if element in lst:         # if element is repeated
            continue               # do nothing
        else :                     # else if element is not in the list
            lst.append(element)    # append
lst.sort()                         # sort the list (de-indent indicates that you sort when the loop ends)
print(lst)
