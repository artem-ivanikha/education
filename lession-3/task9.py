# На вход скрипта подаются два аргумента
# Первый аргумент - входной файл, второй - выходной файл
# Если оба файла существуют, то скрипт завершает работу
# Если входной файл не существует, то скрипт завершает работу
infile=./filein
outfile=./fileout
verify='true'
i=0
[[ ! -f "$infile" ]] && echo no exist && exit 5
[[ -f "$outfile" ]] && echo "exist" && exit 4 
[[ "" != $(cat $infile|awk 'END{print $0}') ]] &&
echo -en '\n''\n' >> $infile
while read string; do
    i=$((i++))
    if [ $verify == 'true' ]; then
        nostring=$string
        verify='false'
    else
         echo -en "\n$string\n$nostring" >> $outfile
         verify='true'
    fi
done <$infile