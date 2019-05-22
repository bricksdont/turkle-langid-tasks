# turkle-langid-tasks

Download data from rattle:

    ./scripts/download_data.sh

This will also fix some file names to be unique.

Generate tasks from the data:

    ./scripts/generate_hits.sh

Instantiate worker template locally:

    ./scripts/instantiate_worker_template.sh

Then open html/worker_template.instance.html in your browser.