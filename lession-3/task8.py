# Написать скрипт, который принимает на вход в виде аргумента IP-адрес
# Скрипт должен проверить доступность адреса посредством ping три раза и записать в лог один раз за все три проверки:
#  - если хост отвечает:
# день-месяц-год час-минута-секунда myHostChecker: <IP> - UP
# - если хост не отвечает:
# день-месяц-год час-минута-секунда myHostChecker: <IP> - DOWN



file=./task8.log
ipaddr=8.8.8.8
#ipaddr=224.9.9.9
#for
[[ "100%packetloss," == $(ping -w 3 $ipaddr | awk '/'"100% packet loss"'/''{print $6 $7 $8}') ]] &&
echo "$(date +%e-%m-%y" "%H-%M-%S)" ""myHostChecker: $ipaddr down"" ||
echo "$(date +%e-%m-%y" "%H-%M-%S)" ""myHostChecker: $ipaddr - UP"" >> $file