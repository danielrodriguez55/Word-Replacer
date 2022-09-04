
def replace_word():

    str = "Testing Testing does this change, hello hello hello"

    print(str)

    word_to_replace = input("Enter word you want to replace: ")
    word_replacement = input("Enter the word replacement: ")

    print(str.replace(word_to_replace, word_replacement))

replace_word()
