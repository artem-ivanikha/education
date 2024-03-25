# Написать скрипт, который следит за местом на партиции.
# Если свободного места осталось менее 50%, записать в лог об этом в формате
# день-месяц-год час-минута-секунда myDiskChecker: <partition> - less than 50%

# Если свободного места осталось менее 10%, записать в лог об этом в формате
# день-месяц-год час-минута-секунда myDiskChecker: <partition> - less than 10%
part=root
file=./task7.log
touch "$file"
while true; do
    use=$(df | awk '/'"$part"'/''{print $5}' | head -1 -c -2 );
    ([[ $use -ge "90" ]] && echo "$(date +%e-%m-%y" "%H-%M-%S)" "myDiskChecker $part - less than 10%" || echo "part $part usage $use""%" ) >> $file
    ([[ $use -ge "50" ]] && echo "$(date +%e-%m-%y" "%H-%M-%S)" "myDiskChecker $part - less than 50%" || echo "part $part usage $use""%" ) >> $file
    sleep 1
done