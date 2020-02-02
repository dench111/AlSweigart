#  Удаление ненужных файлов
#  Напишите программу, которая обходит дерево папок, выполняя поиск исключительно больших
#  по своим размерам файлов и папок, размеры которых > 100 Мб. Выведите абсолютные пути доступа к этим файлам на экран

import shutil, os, StProj_2_Folders

searchDir = StProj_2_Folders.params['Директория с файлами для поиска']
print('Директория с файлами для поиска ' + searchDir)

fileSearchSize = StProj_2_Folders.params['Искать файлы с размером Мб >=']
fileSizeinBytes = int(fileSearchSize) * 2 ** 20
print('Искать файлы с размером >= ' + str(fileSizeinBytes) + ' байт')

if os.path.exists(searchDir):
    for foldername, subfolders, filenames in os.walk(searchDir):
        for subfolder in subfolders:
            print('')
        for filename in filenames:
            location = foldername + '\\' + filename  # определение полного пути + названия файла
            if os.path.getsize(location) >= fileSizeinBytes:
                fileSizeinMbytes = os.path.getsize(location) // (2 ** 20)
                print('Найден файл: ' + location + ' с размером: ' + str(os.path.getsize(location)) +
                      ' байт/ ' + str(fileSizeinMbytes) + ' Мбайта')
                fileList = 'Найден файл: ' + location + ' с размером: ' + str(os.path.getsize(location)) + \
                           ' байт/ ' + str(fileSizeinMbytes) + ' Мбайта \n'
                fileListInFile = open('filelist.txt', 'a')
                fileListInFile.write(fileList)
                fileListInFile.close()
