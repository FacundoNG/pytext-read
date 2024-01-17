

def main():
    textdir = "books/"
    filename = f"{textdir}frankenstein.txt"
    with open(filename) as f:
        textfile = f.read()

    wordcount = count_words(textfile)
    letter_dict = count_letters(textfile)
    sorted_letters =  list(count_letters(textfile))
    sorted_letters.sort()

    print(f"*** Reading through the file: {filename}\n\n*** Starting report:")
    print(f"- The file provided contains {wordcount} words\n")
    for char in sorted_letters:
        print(f"- The character '{char}' was found {letter_dict[char]} times.")
    print("\n*** Report completed")

    
def count_words(text):    
    wordcount = text.split()
    return len(wordcount)

def count_letters(text):
    text = text.lower()
    letters = dict()
    for char in text:
        if char.isalpha() and char not in letters:
            letters[char] = 1
        elif char.isalpha():
            letters[char] += 1
    return letters

main()