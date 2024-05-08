#nc -e /root/nc.sh -lvk 46.243.182.16 60
file=./1.log
touch "$file"
log() {
    port=60
    time=$(date +"%Y-%m-%d %H-%M-%S") 
    remote_ip=$(netstat -ant | grep ':$port' | awk '{print $5}' | cut -d: -f1 | grep -v '^0.0.0.0$') 
    local_ip=$(hostname -I)
    echo "$time $local_ip $remote_ip $command Successfully" > $file
}
while true; do
      read command
      adapter=$(echo $command | awk '{print $2}')
      speed=$(echo $command | awk '{print $3}')
      duplex=$(echo $command | awk '{print $4}')
      #echo $command
        if [[ "$command" == "getDate" ]]; then #то должен выдать текущую дату в формате ГОД-МЕСЯЦ-ДЕНЬ ЧАС-МИНУТА>
         result=$(date +%y-%m-%d" "%H-%M) && log "" && $result
        elif [[ "$command" == "getEpoch" ]]; then #то должен выдать время в unixtime
         date +%s && log ""
        elif [[ "$command" == "getInetStats" ]]; then #то отдаем статистику всех сетевых карт
         echo nmcli device show && log ""
        elif [[ "$command" == getInetStats* ]]; then  #adaptername then #то отдаем статистику указанной сетевой>
         echo nmcli connection show $adapter;
         log ""
        elif [[ "$command" == setSettings* ]]; then # <имяКарты> <duplex> <speed> then #то выставляем указанной>
         echo nmcli connection modify $adapter 802-3-ethernet.speed $speed 802-3-ethernet.duplex $duplex && log ""
        elif [[ "$command" == "bye" ]]; then #то завершить сессию
         exit 0 && log ""
        fi
done
