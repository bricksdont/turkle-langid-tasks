#! /bin/bash

scripts=`dirname "$0"`
base=$scripts/..

data=$base/data
csv_folder=$base/csv

mkdir -p $csv_folder

python3 $scripts/generate_hits.py \
        --folder $data \
        --csv-output $csv_folder/batch.csv \
        --num-per-system 100
