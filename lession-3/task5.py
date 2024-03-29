# Напишите скрипт, который использует один текстовый файл как источник данных
# Файл имеет формат:
# userName creationDate deletionDate homeDir
# userName записывается в виде одного слова
# creationDate записывается в формате unix timestamp 
# deletionDate записывается в формате unix timestamp, если пользователь не удалён, то используется символ тире
# homeDir - путь к домашней директории пользователя
# Напишите функции просмотра информации о пользователе(1), создания пользователя(2), удаления пользователя (3). Используйте case для аргументов скрипта:
# Аргументы скрипта:
#  - s имяПользователя
#  - c имяПользователя
#  - d имяПользователя
#  - h путьКДомашнейДиректории
#  - a 
# s - выводит информацию о пользователе
# c - добавляет пользователя с указанной в аргументе h домашней директории в файл и текущей датой
# d - изменяет deletionDate с тире на текущую дату
# a - выводит список всех пользователей в формате
# Номер строки: имяПользователя датаСоздания датаУдаления путьКДомашнейДиректории


#username=kashkarov
#функции объявлены
file=task5.txt
clear # Очистка экрана
echo  - s имяПользователя
echo  - c имяПользователя
echo  - d имяПользователя
echo  - h путьКДомашнейДиректории
echo  - a 
echo s - выводит информацию о пользователе
echo c - добавляет пользователя с указанной в аргументе h домашней директории в файл и текущей датой
echo d - изменяет deletionDate с тире на текущую дату
echo a - выводит список всех пользователей в формате

userinfo ()
{
  cat $file | head -1;
  grep $username $file
}
mkuser ()
{
 echo "$username"" ""$(date +%s)"" ""-"" ""$userdir" >> $file
} 
rmuser ()
{
  #grep $username $file | awk '{gsub(/........../, "-", $3)}1'
  sed -i "s/-/$(date +%s)/g" $file
}
echo введите аргумент и имя пользователя
read args username userdir
#починить чтобы дважды аргумент смог принять
case "$args" in
  "s" ) # s - выводит информацию о пользователе
  userinfo 
  ;;
 "c" ) # c - добавляет пользователя с указанной в аргументе h домашней директории в файл и текущей датой
  mkuser
  ;;
 "d" ) # d - изменяет deletionDate с тире на текущую дату
  rmuser
  ;;
  "h" ) # h путьКДомашнейДиректории
   userdir=$(cat $file | awk '/'"$username"'/''{print $4}')
  ;;
 "a" )
   cat -n $file
  ;;
          * )
   echo "аргумент не указан"
  ;;
esac

# exit 0

#echo ivanikha    1332468005 1332468005 /home/ivanikha | awk '{gsub(/........../, "-", $4)}1'