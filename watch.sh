clear

echo $1

#
#python3 $1
#$list=$(ls -l)
#| fgrep watch.sh)

touch watch.txt
#echo $last
#exit
while test 1
do
    if test ./watch.txt -ot $1
    then
        touch ./watch.txt; 
        #echo "updated";
        echo
        echo
        python3 ./$1
    fi
    #watch -g -t 'ls -l | fgrep watch.sh'  
    #echo "hello world"; 
    sleep 1
done