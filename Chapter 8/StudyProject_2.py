#  Удаление ненужных файлов
#  Напишите программу, которая обходит дерево папок, выполняя поиск исключительно больших
#  по своим размерам файлов и папок, размеры которых > 100 Мб. Выведите абсолютные пути доступа к этим файлам на экран

import shutil, os, StProj_2_Folders.py

searchDir = StProj_2_Folders.params['Директория с файлами для поиска']
print(searchDir)

fileSearchSize = StProj_2_Folders.params['Искать файлы с размером >=']
print(fileSearchSize)