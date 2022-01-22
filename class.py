# program to take input for the file name from the user and the count the number of word 
#  and senteces 

filename = input('Enter the filename')

filepointer = open(filename, 'r')
text = filepointer.read()

sentence = text.split('.')
words = text.split()
numberOfsentences = len(sentence)
numberOfWords = len(words)

print("number of sentences in the file are " , numberOfsentences)
print("Number of words in the file are ",numberOfWords)
