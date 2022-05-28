# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



def value_to_set(value):
    set_value = set(value)
    set_value = filter(lambda letter: letter.isalpha(), set_value)
    set_value = [letter.lower() for letter in set_value]
    return set(set_value)


def find_anagram(word, anagram):
    # [assignment] Add your code here
    
    word_set = value_to_set(word)
    anagram_set = value_to_set(anagram)

    return not bool(word_set.symmetric_difference(anagram_set))


print(find_anagram('I am Lord Voldemort','Tom Marvolo Riddle'))
