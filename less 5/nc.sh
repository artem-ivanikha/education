#nc -e /root/ether.sh -lvk 46.243.182.16 60
while true; do
      read command
      adapter=$(echo $command | awk '{print $2}')
      speed=$(echo $command | awk '{print $3}')
      duplex=$(echo $command | awk '{print $4}')
        if [[ "$command" == "getDate" ]]; then #то должен выдать текущую дату в формате ГОД-МЕСЯЦ-ДЕНЬ ЧАС-МИНУТА>
         date %y-%m-%e %H-%M
        elif [[ "$command" == "getEpoch" ]]; then #то должен выдать время в unixtime
         date +%y-%m-%d" "%H-%M
        elif [[ "$command" == "getInetStats" ]]; then #то отдаем статистику всех сетевых карт
         nmcli device show
        elif [[ "$command" == getInetStats* ]]; then  #adaptername then #то отдаем статистику указанной сетевой>
         echo nmcli connection show $adapter
        elif [[ "$command" == setSettings* ]]; then # <имяКарты> <duplex> <speed> then #то выставляем указанной>
         echo nmcli connection modify $adapter 802-3-ethernet.speed $speed 802-3-ethernet.duplex $duplex
        elif [[ "$command" == "bye" ]]; then #то завершить сессию
         exit 0
        fi
done