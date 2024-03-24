# Создайте файл со списком пользователей. С помощью for выведите на экран содержимое файла с нумерацией строк
file="./task4.txt"
n=1
for string in $(cat $file)
do
    echo "$n $string"
    let "n++"
done