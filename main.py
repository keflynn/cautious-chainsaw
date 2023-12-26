with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    def word_count(contents):
        word_list = contents.split()
        return len(word_list)
    
    def letter_count(contents):
        letter_dict = {}
        contents_lowered = contents.lower()
        for char in contents_lowered:
            if char in letter_dict:
                letter_dict[char] += 1
            else:
                letter_dict[char] = 1
        return letter_dict
    
    def print_report(contents):
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count(contents)} words found in the document")
        print()

        letter_freqs = letter_count(contents)
        letter_freq_list = []
        for letter in letter_freqs:
            if letter.isalpha():
                letter_freq_list.append((letter_freqs[letter], letter))

        letter_freq_list.sort()
        for i in range(len(letter_freq_list) - 1, -1, -1):
            print(f"The letter '{letter_freq_list[i][1]}' appeared {letter_freq_list[i][0]} times")
        
        print("--- End Report ---")

    print_report(file_contents)
    