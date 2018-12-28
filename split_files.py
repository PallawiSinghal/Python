i=0; 
for f in *; 
do 
    d=dir_$(printf %03d $((i/"number of files needed in each folder"+1))); 
    mkdir -p $d; 
    mv "$f" $d; 
    let i++; 
done
