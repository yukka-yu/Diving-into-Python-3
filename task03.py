text = '''Родился в Питтсбурге, штат Пенсильвания, в семье Ширли (в девичестве Темелес, англ. Shirley L. Temeles, 1926—2012), радиодиктора, которая позже управляла фирмой по продаже кухонного оборудования, и Гарольда Голдблюма (англ. Harold Goldblum, 1920—1983), врача-терапевта[3][4][5]. У Джеффа есть сестра Памела (англ. Pamela) и старший брат Ли (англ. Lee). Ещё один старший брат, Рик (англ. Rick), умер в возрасте 23 лет.'''
AMOUNT = 10

plain_text = text.lower()

for i in [',', '.', ';', '[', ']', '(', ')', '-', '—', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '"', '/']:
    plain_text = plain_text.replace(i, '')

word_list = plain_text.split(' ')
word_set = set(word_list)

max_word_list = []

for _ in range(AMOUNT):

    max_count = 0
    max_word = ''

    for word in word_set:
        count = word_list.count(word)
        if count > max_count:
            max_count = count
            max_word = word
    max_word_list.append(max_word)

    for _ in range(max_count):
        word_list.remove(max_word)

    word_set = set(word_list)  

print(max_word_list)  
