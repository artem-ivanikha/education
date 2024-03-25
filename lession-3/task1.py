#Напиши скрипт, который будет спрашивать имя пользователя и на основе ввода показывать нужную строчку из /etc/passwd.
    #Так же скрипт выводит построчно:
    echo имя пользователя?
    read username
      echo шелл пользователя
      grep '^'$username /etc/passwd | awk -F: '{ print $NF }';
      echo домашнюю директорию пользователя
      grep '^'$username /etc/passwd | awk -F: '{ print $(NF-1) }'; 
      echo список групп, в которых он состоит 
      groups $username | awk '{$1=""; $2=""; print $NF}';
       #После этого скрипт должен спросить, что следует поменять – uid, домашнюю директорию или группу
       echo "who change dir or uid or groups?"
        read chg
        if [[ "$chg" == "uid" ]]; then
            #Если uid, то сначала проверить, доступен ли такой uid, если нет – то один раз предложить ввести заново.
            echo введите желаемый uid
            read uidchk
             if [[ $(awk -F ":" '{print $3}' /etc/passwd | grep ^$uidchk$) == "" ]]; then
             echo usermod -u $uidchk $username     
             else
             echo uid $uidchk занят, введите другой
                read uidchk
                echo usermod -u $uidchk $username
             fi
        #Если группу – то следует спросить, меняем ли мы основную группу или дополнительную.
        elif [[ "$chg" == "groups" ]]; then
            #какую группу меняем?
            echo меняем ли main or secondary?
            read grp
             if [[ "$grp" == "main" ]]; then
             echo usermod -g groupname $username
             elif [[ "$grp" == "secondary" ]]; then
             echo usermod -aG groupname $username
             fi
        #Если домашнюю директорию, то спросить, на какую директорию следует сменить, а также следует ли перемещать домашнюю директорию.
        elif [[ "$chg" == "dir" ]]; then
          echo укажите новую директорию
          read chgdir
          echo usermod -d $chgdir $username
          echo "move old home dir? yes or no"
          read dirmv
           if [[ "$dirmv" == "yes" ]]; then
            echo mv -rf $olddir /root/2
           fi
        fi