s=input("Enter a string:")
x=input("Enter character to replace:")
y=input("Enter new character:")
print("Replaced string:",s.replace(x,y))
print("Reversed string:",s[::-1])
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
print("Character frequency:")
for ch in set(s):
    print(ch,":",s.count(ch))
print("Word frequency:")
words=s.split()
for word in set(words):
    print(word,":",words.count(word))