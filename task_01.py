# Задача 1
# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

#1 Вариант：

one_song = my_favorite_songs [:14]
last_song = my_favorite_songs [64:78]
second_song = my_favorite_songs [16:30]
second_song_end = my_favorite_songs [51:62]

print (one_song,'\n', last_song, '\n', second_song, '\n', second_song_end)




