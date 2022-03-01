def anagram(word1, word2):
    count = 0
    for i in word1:
        for j in word2:
            if i == j:
                count += 1
    if count == len(word1):
        print("anagram")
    else:
        print("not")


if __name__ == '__main__':
    string1 = input("enter the first word")
    string2 = input("enter the second string")
    anagram(string1, string2)
