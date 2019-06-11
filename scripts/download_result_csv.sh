#! /bin/bash

# fail if any subprocess fails
set -e

scripts=`dirname "$0"`
base=$scripts/..

results=$base/results

mkdir -p $results

# remove earlier versions of results
rm -rf $results/*.csv

# you will be prompted for your admin password
(source ~/venvs/turkle/bin/activate && python $scripts/download_results.py -u bricksdont --server localhost:7000 --dir $results)
