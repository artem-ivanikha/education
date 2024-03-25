# Написать скрипт, на вход которого подается либо PID, либо имя программы.
# Скрипт постоянно проверяет что программа находится в памяти
# Каждая проверка записывается в лог в формате:
# день-месяц-год час-минута-секунда mySvcChecker: service <имя_сервиса> [isUP|isDown]
# [isUP|isDown] - состояние сервиса

#echo процесс
#read $proc
file=./task6.log
#touch "$file"
proc=ssh-agent
while true; do
    #echo введеный идентификатор "$proc"
    svc=$(ps -Ao pid,comm | awk '/'"$proc"'/''{print $1" "$2}' | head -1)
    pid=$(echo $svc | awk '{print $1}')
    #echo имя сервиса "$pid"
    svvc=$(echo $svc | awk '{print $2}')
    #echo $svvc
    output=$(date +%e-%m-%y" "%H-%M-%S)" ""mySvcChecker: service $svvc";
    #echo $pid
    #echo $chkpid
    ([[ $pid != "" ]] && echo "$output isUP" || echo "$output isDown") >> $file
    sleep 1
done



