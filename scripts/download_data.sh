#! /bin/bash

scripts=`dirname "$0"`
base=$scripts/..

data=$base/data

mkdir -p $data

for folder in translations_baseline translations_bilingual translations_fine_tuned translations_pivot; do

    mkdir -p $data/$folder

    scp mmueller@rattle.ifi.uzh.ch:/home/user/arios/low_resource/$folder/*.detok $data/$folder

done

# fix names of baseline, bilingual, pivot (fine_tuned files have correct names)
# caution: do not run twice without deleting old files

for folder in baseline bilingual pivot; do

    for file in $data/translations_"$folder"/*; do

        base_name=`basename $file .detok`
        new_name="$base_name"."$folder".detok

        mv $file $data/translations_"$folder"/$new_name

    done
done

# sizes
echo "Sizes of files:"
for folder in translations_baseline translations_bilingual translations_fine_tuned translations_pivot; do
	echo "folder: "$folder
	wc -l $data/$folder/*
done
