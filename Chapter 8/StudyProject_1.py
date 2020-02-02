# Выборочное копирование.
# Напишите программу, выполняющую обход дерева каталогов с целью отбора файлов с заданным расширением.
# Скопируйте эти файлы из их текущего расположения в новую папку

# Входные данные:
# Исходный и целевые каталоги, а также задание расширения для выбора копируемых файлов
# задаются в модуле 'StProj_1_Folders'

import shutil, os, StProj_1_Folders

SourceDir = StProj_1_Folders.folders['Директория с исходными файлами']
TargetDir = StProj_1_Folders.folders['Целевая директория для копирования']
FileExt = StProj_1_Folders.folders['Расширение файла']
print('Директория с исходными файлами: ' + SourceDir)
print('Целевая директория для копирования: ' + TargetDir)
print('расширение копируемых файлов: ' + FileExt)

for foldername, subfolders, filenames in os.walk(SourceDir):
    for subfolder in subfolders:
        print('')
    for filename in filenames:
        location = foldername + '\\' + filename  # определение полного пути + названия файла
        if filename.endswith(FileExt) == True:
            print('Пытаюсь скопировать файл: ' + location)
            if os.path.exists(TargetDir) == True:  # проверка существования целевой директории
                shutil.copy(f"{location}", TargetDir)
                print('Файл ' + location + ' скопирован')
                print('')
            else:
                print('Ошибка при копировании!!! Директории ' + TargetDir + ' не существует')
                print('')
                continue
