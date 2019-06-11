#! /bin/bash

scripts=`dirname "$0"`
base=$scripts/..

results=$base/results

python3 $scripts/evaluate.py --csv $results/batch-Batch_1_results.csv
