# Написать скрипт, который принимает на вход два аргумента: <path> <time>
# Скрипт должен вывести список файлов из <path> старше <time>
# <time> может быть задан в любом формате, который понимает утилита date

path=~/git/education/
time="24-03-21 16:10:09"
#time=$(echo "укажите время" date +%e-%m-%y" "%H:%M:%S)"
#find $path -not -newermt "24-03-21 16:00"
find $path -not -newermt "$time"