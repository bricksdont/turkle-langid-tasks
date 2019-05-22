#!/bin/bash

# replace template variables in html for testing,
# as Turkle would do before it serves to workers.

scripts=`dirname "$0"`
base=$scripts/..

html=$base/html

cat $html/worker_template.html | \
    sed 's/${text}/"Kommission Kommission sucht portugiesische Beihilfen für die Sammlung,, örderung,, und VerVertung von Schlachabfällen"/g' \
    > $html/worker_template.instance.html
