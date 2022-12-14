# Задача 1
# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

#1 Вариант：

first_song = my_favorite_songs [:14]
last_song = my_favorite_songs [64:78]
second_song = my_favorite_songs [16:30]
previous_song = my_favorite_songs [51:62]

print (first_song,'\n', last_song, '\n', second_song, '\n', previous_song)

#2 Вариант：

first_song = my_favorite_songs [ : my_favorite_songs.find(',')]
last_song = my_favorite_songs [my_favorite_songs.rfind('N') : ]
second_song = my_favorite_songs [my_favorite_songs.find('S') : my_favorite_songs.find(', A')]
previous_song = my_favorite_songs [my_favorite_songs.rfind('Start') : my_favorite_songs.rfind(',')]

print (first_song,'\n', last_song, '\n', second_song, '\n', previous_song)


#3 Вариант：

songs = my_favorite_songs.split(',') 

print (songs[0], songs[-1], songs[1], songs[-2])