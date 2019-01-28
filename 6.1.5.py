word = "hello world"
print ("hello"==word[0:5])
print (word.startswith("hello"))
print (word.endswith("ld",6))
print (word.endswith("ld",6,10))
print (word.endswith("ld",6,len(word)))