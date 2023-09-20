def function_volume_letters(phrase, letters):
    volume_of_letters = []
    count = 0
    for i in phrase + " ":
        if i in letters:
            count += 1
        if i == (" "):
            volume_of_letters.append(count)
            count = 0
    return volume_of_letters

letters = "ауоиэыяюеё"  # Гласные -«а» «у» «о» «и» «э» «ы» «я» «ю» «е» «ё»
phrase = input("Введите строку ")

if len(set(function_volume_letters(phrase, letters))) < 2:
    print("Парам пам-пам")
else:
    print("Пам парам")
