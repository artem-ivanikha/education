echo "input filename"
read file
echo "input right user r-read;w-write;x-execute;X-special execute" 
read accu
echo "input right group r-read;w-write;x-execute;X-special execute"
read accg
echo "input right other user r-read;w-write;x-execute;X-special execute"
read acco
echo "mk $file && chmod u=$accu,g=$accg,o=$acco $file"