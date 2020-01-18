> train1.list
> test1.list
COUNT=-1
echo "第一个参数为 $1"
echo "第二个参数为 $2"
for folder in $1/*
do
    COUNT=$[$COUNT + 1]
    for imagesFolder in "$folder"/*
    do
      echo "$imagesFolder" $COUNT >> test1.list
    done
done