 string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
words1 = string1.split()
words2 = string2.split()
all_words = set(words1 + words2)
uncommon_words = [word for word in all_words if (word in
words1) ^ (word in words2)]
print("Uncommon words:", uncommon_words)