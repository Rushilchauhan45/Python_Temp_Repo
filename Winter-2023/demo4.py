#Write following Python functions:
# • Function-1: Returns reverse string word-wise.
# • Function-2: Count occurrence of vowels from input string.
# Design main Python code where above functions are called.

# [7 makrs]

def reverse_fun(s):
    words = s.split()
    rev_words = ' '.join(reversed(words))
    return rev_words

def vowels_count(s):
    vowels = "aeiouAEIOU"
    count = 0 
    for i in s:
        if i in vowels:
            count = count + 1
    return count        


# ----------Main Code Starts Here----------

sentence = input("Enter a sentence: ")

rev = reverse_fun(sentence)
vowels = vowels_count(sentence)


print("Reversed sentence word-wise:", rev)
print("Number of vowels in the sentence:", vowels)
