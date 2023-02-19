poem = 'пара-ра-рам рам-пам-папам па-ра-па-дам'


def check_rhythm(string_of_words):
    vowels = 'аеёиоуыэюя'
    list_of_count_vowels = \
        [sum(letter in vowels for letter in string_of_words) for string_of_words in string_of_words.split()]
    return 'Парам пам-пам' if len(set(list_of_count_vowels)) == 1 else 'Пам парам'


print(check_rhythm(poem))
