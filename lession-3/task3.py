echo "input way to blk device"
#read waybllk

mntpoint=$(mount | grep $waybllk | awk -F " " '{print $3}') #не учитывает переменную wayblk
echo $mntpoint
     if [ -z "$mntpoint" ]; then
     echo "устройство не примонтировано"
     #смонтировать устройство
     else
     exit 90
     fi