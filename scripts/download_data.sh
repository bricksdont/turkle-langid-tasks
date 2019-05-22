#! /bin/bash

scripts=`dirname "$0"`
base=$scripts/..

data=$base/data

mkdir -p $data

for folder in translations_baseline translations_bilingual translations_fine_tuned translations_pivot; do

    mkdir -p $data/$folder

    scp mmueller@rattle.ifi.uzh.ch:/home/user/arios/low_resource/$folder/*.detok $data/$folder

done

# sizes
echo "Sizes of files:"
for folder in translations_baseline translations_bilingual translations_fine_tuned translations_pivot; do
	echo "folder: "$folder
	wc -l $data/$folder/*
done
