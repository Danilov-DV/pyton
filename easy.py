# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os, sys, shutil

#2
def print_dirs():
    print([el for el in os.listdir() if os.path.isdir(el)])

#1
def my_func():
    for i in range(1, 10):
        os.mkdir(f"dir_{i}")
    print_dirs()

    for i in range(1, 10):
        os.removedirs(f"dir_{i}")
    print_dirs()

#3
def copy_this():
    this_ = os.path.basename(sys.argv[0])
    shutil.copy(this_, f"copy_{this_}")


copy_this()

