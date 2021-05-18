from random import sample
# 5. Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или
# запрещающий повторы слов в шутках (когда каждое слово можно использовать
# только в одной шутке)? Сможете ли вы сделать аргументы именованными?


def get_jokes(n, repeat=False):
    """
    get string composed from random words from built-in lists

    :param n: the number of strings
    :param repeat: words in jokes can repeat
    """
    if repeat is True:
        for _ in range(n):
            nouns = sample(["автомобиль", "лес", "огонь", "город", "дом"], 1)
            adverbs = sample(["сегодня", "вчера", "завтра", "позавчера", "ночью"], 1)
            adjectives = sample(["веселый", "яркий", "зеленый", "утопичный", "мягкий"], 1)
            for noun, adverb, adjective in zip(nouns, adverbs, adjectives):
                print(f'{noun} {adverb} {adjective}')
    elif repeat is False and n > 5:
        print("can't make it")
    else:
        nouns = sample(["автомобиль", "лес", "огонь", "город", "дом"], n)
        adverbs = sample(["сегодня", "вчера", "завтра", "позавчера", "ночью"], n)
        adjectives = sample(["веселый", "яркий", "зеленый", "утопичный", "мягкий"], n)
        for noun, adverb, adjective in zip(nouns, adverbs, adjectives):
            print(f'{noun} {adverb} {adjective}')


get_jokes(6, True)
