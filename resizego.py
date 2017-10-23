#!/usr/bin/python
# -*- coding: utf-8

#import
import subprocess # эта библиотека позволяет использовать bash из python

# ФУНКЦИИ

# использование imagemagick для изменения размера картинок
def resizeimg(image_name, image_type, size):
    subprocess.call('convert ' + image_name + image_type + ' -resize ' + size + ' img'+ size + image_type, shell=True)

# читаем файл и заносим значение в массив
def read_file(f):
    out = []
    for line in f:
       row = [int(i) for i in line.split()]
       out.append(row)
    return out


# ТЕЛО

mode_type = input('Запустить программу с настройками по умолчанию [1] или с пользовательскими параметрами [2]?: ')
if mode_type == '2':
    # ввод названия картинки
    image_name =input('Введите название изображения (без расширения): ')
    # если пользователь ничего не ввел, то по умолчанию название файла - original
    if image_name == '':
        image_name = 'original'

    # ввод расширения картинка
    image_type =input('Введите расширение изображения: ')
    # если пользователь ничего не ввел, то по умолчанию расширение файла - jpg
    if image_type == '':
        image_type = '.jpg'
    elif image_type[0] != '.':
        image_type = '.' + image_type

    # ввод названия файла, где хранятся ширины
    size_file_name =input('Введите название файла с размерами изображений (с расширением): ')
    # если пусто, то указываем значение по умолчанию
    if size_file_name == '':
        size_file_name = 'sizes.txt'
    archieve_name =input('Как назвать папку с архивом: ')
    # если пусто, то указываем значение по умолчанию
    if archieve_name == '':
        archieve_name = 'resized_images'
else:
    image_name = 'original'
    image_type = '.jpg'
    size_file_name = 'sizes.txt'
    archieve_name = 'resized_images'

# вызываем фукнцию дабы записать значение файла в массив
array = read_file(open(size_file_name))
# считываем размер массива
array_length  = len(array[0])

# создаем новую папку, куда будем класть картинки
subprocess.call('mkdir resized_images', shell=True)
subprocess.call('cp ' + image_name + image_type + ' ./resized_images/', shell=True)



# вызываем функцию дабы изменить размер картинки
for x in range(0, array_length):
    resizeimg(image_name, image_type, str(array[0][x]))
#
subprocess.call('mv img* ./resized_images', shell=True)
subprocess.call('zip ' + archieve_name + '.zip -r ./resized_images', shell=True)
subprocess.call('rm -rf ./resized_images', shell=True)


# смотрим содержимое папки
subprocess.call('ls', shell=True)




